from django.contrib import admin
from players.models import Player
from players.forms import PlayerAdminForm
from imagekit.admin import AdminThumbnail


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    form = PlayerAdminForm
    list_display = ('nickname', 'photo_thumbnail', 'tagline', 'registration_date')
    search_fields = ('nickname', 'tagline')
    fieldsets = (
        ('Player', {'fields': (('nickname', 'password'), ('photo', 'photo_thumbnail', ), ('tagline', 'audio'), ), }), )
    readonly_fields = ('photo_thumbnail', )
    ordering = ['-registration_date']

    photo_thumbnail = AdminThumbnail(image_field='photo_thumb', template='../templates/admin_lightbox/players_photos.html')
    photo_thumbnail.short_description = 'Miniatura foto'
