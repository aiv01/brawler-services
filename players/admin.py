from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from players.models import Player
from imagekit.admin import AdminThumbnail


@admin.register(Player)
class PlayerAdmin(UserAdmin):
    list_display = ('username', 'tagline', 'photo_thumbnail', 'ip', 'port', 'registration_date')
    search_fields = ('username', 'tagline', 'ip', 'port')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('Dati', {'fields': (('username', 'registration_date'), ('photo', 'photo_thumbnail', ), ('tagline', 'audio'), ), }),
        ('Endpoint', {'fields': (('ip', 'port'), ), }),
        ('Password', {'fields': (('password', ), ('token', ), ), }),
        ('Privilegi', {'fields': (('is_active', 'is_staff', 'is_superuser'), ), }), )
    readonly_fields = ('registration_date', 'ip', 'port', 'token', 'photo_thumbnail', )
    ordering = ['-registration_date']

    photo_thumbnail = AdminThumbnail(image_field='photo_thumb', template='../templates/admin_lightbox/players_photos.html')
    photo_thumbnail.short_description = 'Miniatura foto'
