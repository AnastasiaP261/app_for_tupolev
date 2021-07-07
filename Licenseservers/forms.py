from django import forms
from .models import Licenseservers


# class LicenseserversForm(forms.Form):
#     choices = list(Licenseservers.objects.values_list('site', flat=True).distinct())
#     choices.insert('Все', 0)
#     select = forms.ChoiceField(choices=["all"], widget=forms.RadioSelect)
