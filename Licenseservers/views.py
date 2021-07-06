from django.shortcuts import render
from django.views.generic import ListView
from .models import Licenseservers


class ViewLicenses(ListView):
    model = Licenseservers

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewLicenses, self).get_context_data(**kwargs)
        return context
