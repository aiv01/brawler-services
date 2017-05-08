from django.contrib import admin
from servers.models import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip', 'port', 'country', 'city', 'time_zone')
    search_fields = ('ip', 'port', 'country', 'city', 'time_zone')
    list_filter = ('country', 'city', 'time_zone')
    fieldsets = (
        ('Server', {'fields': (('ip', 'port'), ), }),
        ('Location', {'fields': ('country', 'city', 'time_zone', ), }),
        ('Position', {'fields': ('latitude', 'longitude', ), }), )
    readonly_fields = ('country', 'city', 'time_zone', 'latitude', 'longitude', )
