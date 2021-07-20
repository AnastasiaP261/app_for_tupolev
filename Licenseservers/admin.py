from django.contrib import admin
from .models import Licenseservers


class LicensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'host', 'port', 'creation', 'total_auth', 'total_cons', 'site')
    list_filter = ('site', )


admin.site.register(Licenseservers, LicensesAdmin)
