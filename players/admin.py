from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from players.models import Player, PlayerDefaultImages
from imagekit.admin import AdminThumbnail


@admin.register(Player)
class PlayerAdmin(UserAdmin):
    list_display = ('username', 'tagline', 'photo_thumbnail', 'ip', 'port', 'last_login', 'registration_date')
    search_fields = ('username', 'tagline', 'ip', 'port')
    date_hierarchy = 'registration_date'
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('Dati', {'fields': (('username', ), ('photo', 'photo_thumbnail'), ('tagline', 'audio'), ('last_login', 'registration_date'), ), }),
        ('Endpoint', {'fields': (('ip', 'port'), ), }),
        ('Password', {'fields': (('password', ), ('token', ), ), }),
        ('Privilegi', {'fields': (('is_active', 'is_staff', 'is_superuser'), ), }), )
    readonly_fields = ('last_login', 'registration_date', 'ip', 'port', 'token', 'photo_thumbnail')
    ordering = ['-registration_date']

    photo_thumbnail = AdminThumbnail(image_field='photo_thumb', template='../templates/admin_lightbox/players_photos.html')
    photo_thumbnail.short_description = 'Miniatura foto'


@admin.register(PlayerDefaultImages)
class PlayerDefaultImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumb', 'last_modified')
    date_hierarchy = 'last_modified'
    fieldsets = (
        ('Titolo immagine', {'fields': ('title', ), }),
        ('Immagine di default', {'fields': (('image', 'image_thumb'), ), }), )
    readonly_fields = ('image_thumb', )
    ordering = ['-last_modified']

    image_thumb = AdminThumbnail(image_field='image_thumb', template='../templates/admin_lightbox/players_default_images.html')
    image_thumb.short_description = 'Miniatura immagine'
