from django.contrib import admin
from mobile.models import Audio


@admin.register(Audio)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('mobile_id', 'audio')
    search_fields = ('mobile_id', )
    fieldsets = (
        ('Audio', {'fields': (('mobile_id', 'audio'), ), }), )
