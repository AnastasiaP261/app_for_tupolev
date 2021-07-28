import os
from collections import defaultdict
from random import randint

import openpyxl
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from Licenseservers.models import *
from Users.models import *
from my_app.settings import FILE_FOR_PROC_REQUESTS
from .forms import *


class ViewAddingOrders(TemplateView):
    template_name = 'adding_orders.html'

    def get(self, request, *args, **kwargs):
        req = self.request.GET
        if req:  # эта часть кода сработает, когда мы отправим данные из формы
            # достаем данные
            form_set = TableFormSet0(req).data
            table = defaultdict(list)
            for inf in form_set:
                key = inf.split('-')[1]
                table[key].append(form_set[inf])

            # валидируем каждую строку
            for key in table:
                self.validate_data(table[key])

            # запись в файл
            # with open(FILE_FOR_PROC_REQUESTS, 'wb', encoding='ascii') as f:
            with open(FILE_FOR_PROC_REQUESTS, 'w', encoding='ansi') as f:
                for key in table:
                    f.write('|'.join(table[key]))
                    f.write('\n')

            # запись в логи
            new_info = ''
            for key in table:
                new_info += '|'.join(table[key][1:]) + '\n'

            Logs(info=new_info,
                 sd_number=table[key][0],
                 session_id=os.getlogin(),
                 action='something'
                 ).save()

            return redirect('menu')
        # эта часть кода сработает чтобы отобразить таблицу в начальном состоянии
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # помещаем данные из сессии в контекстную переменную
        if self.request.session.get('table_data') != None:
            context['form_set'] = TableFormSet0(initial=self.request.session.get('table_data'))
        else:
            context['form_set'] = TableFormSet1()

        try:  # чистим сессию
            del self.request.session['table_data']
        except KeyError:
            pass

        # вставка полей для подсказок
        context['sites'] = Licenseservers.objects.values_list('site', flat=True).distinct()
        context['lic_servers'] = Licenseservers.objects.values_list('name', flat=True).distinct()

        return context

    def validate_data(self, data: list):  # функция для валидации строки таблицы
        def valid_req_name(dat):  # валидация номера заявки
            return False

        def valid_full_name(dat):  # валидация фио
            return False

        if valid_req_name(data[1]):
            raise ValidationError('текст ошибки', code='код ошибки')

        if valid_full_name(data[0]):
            raise ValidationError('текст ошибки', code='код ошибки')
        # и так далее...


class ViewGroupmembers(ListView):
    model = Users

    def get_context_data(self, *args, object_list=None, **kwargs):
        # кладем все нужное в контекстную переменную
        context = super().get_context_data(**kwargs)

        context['names'] = Users.objects.values_list('fullname', flat=True).order_by('fullname').distinct()
        context['tcnames'] = Users.objects.values_list('tcname', flat=True).order_by('tcname').distinct()
        context['table_print'] = len(self.request.GET) != 0

        return context

    def get_queryset(self):
        req = self.request.GET
        sql_request = '''
            SELECT 
            us.id,
            us.fullName as fullname,
            us.tcName as tcname,
            us.osName as osname,
            gm.group,
            gm.role,
            us.lastLogin as lastlogin,
            us.licenseServer as licserver,
            us.site as site, 
            us.status   
            
            FROM tcusers.users us right join tcusers.groupmembers gm on us.tcName = gm.tcName and us.site = gm.site
        '''

        if req:
            sql_request += '\nWHERE '
            params = []
            if req['fullname_choice'] != '':
                sql_request += 'fullname=%s'
                params.append(self.request.GET['fullname_choice'])
                if req['tcname_choice'] != '':
                    sql_request += ' and '

            if req['tcname_choice'] != '':
                sql_request += 'us.tcName=%s'
                params.append(self.request.GET['tcname_choice'])

            data = Users.objects.raw(sql_request, params=params)
            return data

        data = Users.objects.raw(sql_request)
        return data


def upload_excel(request):
    if request.method == 'POST' and request.FILES['file']:
        # обработка данных полученных из формы
        file = request.FILES['file']
        table_data = handle_uploaded_file(file)

        # поместим полученные данные из файла в сессию
        request.session['table_data'] = table_data

        return redirect('adding_orders')  # будет вызван метод get_context_data класса ViewAddingOrders
    else:
        # вывод самой формы при первом заходе на страницу
        form = UploadExcelFileForm()
    return render(request, 'adding_excel_file.html', {'form': form})


def handle_uploaded_file(f):
    try:
        ex_file = openpyxl.load_workbook(f)
    except:
        raise ValidationError('Invalid format', code='invalid')

    sheet = ex_file.get_sheet_by_name(ex_file.get_sheet_names()[0])

    table_data = []

    req_num = sheet['A2'].value
    for row in range(2, sheet.max_row + 1):
        trans_name = transliterate(sheet[(f"B{row}")].value.split(' ')[1][:1]) \
                     + transliterate(sheet[(f"B{row}")].value.split(' ')[0])
        trans_name = trans_name.lower()

        table_data.append({
            'req_num': f'{req_num}',
            'full_name': f'{sheet[(f"B{row}")].value}',
            'os_name': f'{sheet[(f"F{row}")].value}',
            'tc_name': f'{trans_name}',
            'tc_pass': f'{trans_name + str(randint(111, 999))}',
            'group': f'{sheet[(f"D{row}")].value}',
            'role': f'{sheet[(f"E{row}")].value}',
            'lic_server': f'{sheet[(f"G{row}")].value}',
            'site': f'{sheet[(f"H{row}")].value}',
        })

    return table_data


def transliterate(name):
    # Слоаврь с заменами
    slovar = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
        'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
        'ю': 'yu', 'я': 'ya',

        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
        'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
        'Ю': 'Yu', 'Я': 'Ya',

        ' ': ' ',
    }

    # Циклически заменяем все буквы в строке
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name
