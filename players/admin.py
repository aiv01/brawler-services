from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from players.models import Player, PlayerDefaultImages
from imagekit.admin import AdminThumbnail
from match.models import Match


@admin.register(Player)
class PlayerAdmin(UserAdmin):
    list_display = ('username', 'tagline', 'photo_thumbnail', 'ip', 'port', 'match_won_count', 'match_partecipated_count', 'last_login', 'registration_date')
    search_fields = ('username', 'tagline', 'ip', 'port')
    date_hierarchy = 'registration_date'
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('Dati', {'fields': (('username', ), ('photo', 'photo_thumbnail'), ('tagline', 'audio'), ('last_login', 'registration_date'), ), }),
        ('Endpoint', {'fields': (('ip', 'port'), ), }),
        ('Password', {'fields': (('password', ), ('token', ), ), }),
        ('Privilegi', {'fields': (('is_active', 'is_staff', 'is_superuser'), ), }),
        ('Match vinti', {'fields': (('match_won_count', 'match_won'), ), }),
        ('Match partecipati', {'fields': (('match_partecipated_count', 'match_partecipated'), ), }), )
    readonly_fields = ('last_login', 'registration_date', 'ip', 'port', 'token', 'photo_thumbnail', 'match_won', 'match_partecipated', 'match_won_count', 'match_partecipated_count')
    ordering = ['-registration_date']

    def match_won(self, model):
        return ", ".join([str(match) for match in Match.objects.filter(winner__username=model.username)])
    match_won.short_description = 'Match vinti'

    def match_partecipated(self, model):
        return ", ".join([str(match) for match in Match.objects.filter(participants__username=model.username)])
    match_partecipated.short_description = 'Match Partecipati'

    def match_won_count(self, model):
        return Match.objects.filter(winner__username=model.username).count()
    match_won_count.short_description = 'Match vinti'

    def match_partecipated_count(self, model):
        return Match.objects.filter(participants__username=model.username).count()
    match_partecipated_count.short_description = 'Match Partecipati'

    photo_thumbnail = AdminThumbnail(image_field='photo_thumb', template='../templates/admin_lightbox/players_photos.html')
    photo_thumbnail.short_description = 'Miniatura foto'


@admin.register(PlayerDefaultImages)
class PlayerDefaultImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumb', 'last_modified')
    search_fields = ('title', )
    date_hierarchy = 'last_modified'
    fieldsets = (
        ('Titolo immagine', {'fields': ('title', ), }),
        ('Immagine di default', {'fields': (('image', 'image_thumb'), ), }), )
    readonly_fields = ('image_thumb', )
    ordering = ['-last_modified']

    image_thumb = AdminThumbnail(image_field='image_thumb', template='../templates/admin_lightbox/players_default_images.html')
    image_thumb.short_description = 'Miniatura immagine'
