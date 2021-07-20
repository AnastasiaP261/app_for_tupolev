from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'tcname', 'osname', 'fullname', 'defgroup', 'status', 'lastlogin',
                    'licenseserver', 'licenselevel', 'site', 'deactreason')
    search_fields = ('tcname', 'osname', 'fullname', 'defgroup', 'licenseserver', 'site')
    list_filter = ('status', 'licenseserver', 'site')


class GroupmembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'tcname', 'info', 'group', 'role', 'site')
    list_filter = ('site', 'group', )


admin.site.register(Groupmembers, GroupmembersAdmin)
admin.site.register(Users, UsersAdmin)



