from django.shortcuts import render
from django.views.generic import ListView
from Users.models import *


class ViewGroupmembers(ListView):
    model = Users

    def get_context_data(self, *, object_list=None, **kwargs):
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
            print(self.request.GET)
            if req['fullname_choice'] != '':
                sql_request += 'fullname=%s'
                params.append(self.request.GET['fullname_choice'])
                if req['tcname_choice'] != '':
                    sql_request += ' and '

            if req['tcname_choice'] != '':
                sql_request += 'us.tcName=%s'
                params.append(self.request.GET['tcname_choice'])

            print(params)

            data = Users.objects.raw(sql_request, params=params)
            return data

        data = Users.objects.raw(sql_request)
        return data








