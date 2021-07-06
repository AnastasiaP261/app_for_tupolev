from django.contrib import admin
from .models import Licenseservers


class LicensesAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'port', 'creation', 'total_auth', 'total_cons', 'site')


admin.site.register(Licenseservers, LicensesAdmin)
