from django.contrib import admin
from servers.models import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip', 'port', 'country')
    search_fields = ('ip', 'port', 'country')
    list_filter = ('country', )
    fieldsets = (
        ('Server', {'fields': (('ip', 'port'), ), }),
        ('Location', {'fields': ('country', ), }),
        ('Position', {'fields': ('latitude', 'longitude'), }), )
    readonly_fields = ('country', 'latitude', 'longitude')
