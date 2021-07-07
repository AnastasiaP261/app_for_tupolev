from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Licenseservers
# from .forms import LicenseserversForm


class ViewLicenses(ListView):
    model = Licenseservers

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Licenseservers.objects.values_list('site', flat=True).distinct()
        context['select_site'] = self.request.GET['flexRadioDefault'] if len(self.request.GET) else 'all'
        return context

    def get_queryset(self):
        req = self.request.GET
        if len(req) == 0 or req['flexRadioDefault'] == 'all':
            return Licenseservers.objects.all()
        else:
            return Licenseservers.objects.filter(site=req['flexRadioDefault'])












