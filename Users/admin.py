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


class TcgroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parentname', 'description', 'volume', 'site', 'roles')
    list_filter = ('site', )
    search_fields = ('name', 'parentname')


class LogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time_stamp', 'sd_number', 'info', 'action', 'session_id', )


admin.site.register(Groupmembers, GroupmembersAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Tcgroups, TcgroupsAdmin)
admin.site.register(Logs, LogsAdmin)
