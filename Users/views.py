from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from Users.models import *
from Licenseservers.models import *
from .forms import UploadExcelFileForm
import openpyxl
from django.core.files.storage import FileSystemStorage


class ViewAddingOrders(TemplateView):
    template_name = 'adding_orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sites'] = Licenseservers.objects.values_list('site', flat=True).distinct()
        context['lic_servers'] = Licenseservers.objects.values_list('name', flat=True).distinct()

        return context


class ViewGroupmembers(ListView):
    model = Users

    def get_context_data(self, *args, object_list=None, **kwargs):
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
        file = request.FILES['file']
        handle_uploaded_file(file)
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    # if request.method == 'POST':
    #     form = UploadExcelFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES['file'])
    #         return HttpResponseRedirect('/success/url/')
    else:
        form = UploadExcelFileForm()
    return render(request, 'adding_excel_file.html', {'form': form, 'empty': True})


def handle_uploaded_file(f):
    ex_file = openpyxl.load_workbook(f)
    sheet = ex_file.get_sheet_by_name(ex_file.get_sheet_names()[0])

    table_data = []

    req_num = sheet['A2'].value
    for row in range(2, sheet.max_row + 1):
        table_data.append({
            'req_num': f'{req_num}',
            'full_name': f'{sheet[(f"B{row}")].value}',
            'os_name': f'{sheet[(f"F{row}")].value}',
            'tc_name': f'',
            'tc_pass': f'',
            'group': f'{sheet[(f"D{row}")].value}',
            'role': f'{sheet[(f"E{row}")].value}',
            'lic_server': f'{sheet[(f"G{row}")].value}',
            'site': f'{sheet[(f"H{row}")].value}',
            })

    return redirect('adding_orders', kwargs={'table': table_data})


