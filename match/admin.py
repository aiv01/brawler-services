from django.contrib import admin
from match.models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'winner', 'get_participants', 'server')
    search_fields = ('id', 'winner__username', 'participants__username', 'server__ip', 'server__port', 'server__country')
    date_hierarchy = 'start_date'
    list_filter = (('winner', admin.RelatedOnlyFieldListFilter), ('server', admin.RelatedOnlyFieldListFilter), )
    fieldsets = (
        ('Match', {'fields': (('id', 'server'), ('start_date', 'end_date'), ), }),
        ('Vincitore', {'fields': (('winner', ), ), }),
        ('Partecipanti', {'fields': (('participants', ), ), }), )
    filter_horizontal = ('participants', )
    readonly_fields = ('id', 'start_date')
    ordering = ['-start_date']

    def get_participants(self, model):
        return ", ".join([str(participant) for participant in model.participants.all()])
    get_participants.short_description = 'Partecipanti'
