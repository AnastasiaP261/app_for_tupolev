from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'tcname', 'osname', 'fullname', 'defgroup', 'status', 'lastlogin',
                    'licenseserver', 'licenselevel', 'site', 'deactreason')
    search_fields = ('tcname', 'osname', 'fullname', 'defgroup', 'licenseserver', 'site')
    list_filter = ('status', 'licenseserver', 'site')


admin.site.register(Users, UsersAdmin)



