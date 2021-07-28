from django.views.generic import ListView

from .models import Licenseservers


class ViewLicenses(ListView):
    model = Licenseservers

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Licenseservers.objects.values_list('site', flat=True).distinct()
        context['select_site'] = self.request.GET['select_menu'] if len(self.request.GET) else 'all'
        return context

    def get_queryset(self):
        req = self.request.GET
        if len(req) == 0 or req['select_menu'] == 'all':
            return Licenseservers.objects.all()
        else:
            return Licenseservers.objects.filter(site=req['select_menu'])


class ViewFreeLicenses(ListView):
    model = Licenseservers
    template_name = 'freelicenseservers_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Licenseservers.objects.values_list('site', flat=True).distinct()
        context['lic_names'] = dict()
        context['lic_names']['all'] = Licenseservers.objects.values_list('name', flat=True).distinct()
        for site in context['sites']:
            context['lic_names'][f'{site}'] = Licenseservers.objects.filter(site=site).values_list('name', flat=True).distinct()

        context['select_site'] = self.request.GET['select_menu1'] \
            if 'select_menu1' in self.request.GET else 'all'
        context['select_lic_name'] = self.request.GET['select_menu2'] \
            if 'select_menu2' in self.request.GET else 'all'
        return context

    def get_queryset(self):
        req = self.request.GET
        sql_request = '''
            SELECT 
                lic.id,
                lic.site,
                lic.name, 
                lic.host, 
                lic.total_auth,
                us1.count_auth,
                lic.total_auth - us1.count_auth as difference_author,
                lic.total_cons,
                us2.count_cons,
                lic.total_cons - us2.count_cons as difference_consumer
                
                FROM tcusers.licenseservers lic 
                left join (select 
                        site,
                        licenseServer,
                        licenseLevel,
                        count(*) as count_auth
                            from tcusers.users as us where us.status = 0 and us.licenseLevel = 0 
                            group by us.licenseLevel, us.site, us.licenseServer) as us1
                on lic.name=us1.licenseServer and lic.site = us1.site 
                left join (select 
                        site,
                        licenseServer,
                        licenseLevel,
                        count(*) as count_cons
                            from tcusers.users as us where us.status = 0 and us.licenseLevel = 1 
                            group by us.licenseLevel, us.site, us.licenseServer) as us2
                on lic.name=us2.licenseServer and lic.site = us2.site
            '''
        # если это не первый заход на страницу, то в запросе будут хоть какие то аргументы
        if len(req) != 0:
            # проверка выбраны ли фильтры по сайту и не all ли это
            site_filter = 'select_menu1' in self.request.GET \
                          and self.request.GET['select_menu1'] != 'all'
            # проверка выбраны ли фильтры по лицензии и не all ли это
            name_lic_filter = 'select_menu2' in self.request.GET \
                              and self.request.GET['select_menu2'] != 'all'

            # если оба фильтра выбраны all то нет смысла фильтровать данные, достаточно выполнить исходный запрос
            if site_filter or name_lic_filter:
                sql_request += '\nWHERE '
                params = []

                if site_filter:
                    sql_request += 'lic.site=%s'
                    params.append(self.request.GET['select_menu1'])
                    if name_lic_filter:
                        sql_request += ' and '
                if name_lic_filter:
                    sql_request += 'lic.name=%s'
                    params.append(self.request.GET['select_menu2'])

                data = Licenseservers.objects.raw(sql_request, params=params)
                return data

        data = Licenseservers.objects.raw(sql_request)
        return data
