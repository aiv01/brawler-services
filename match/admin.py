from django.contrib import admin
from match.models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'winner', 'get_participants')
    search_fields = ('id', 'winner__username', 'participants__username')
    date_hierarchy = 'date'
    list_filter = (('winner', admin.RelatedOnlyFieldListFilter), )
    fieldsets = (
        ('Match', {'fields': (('id', 'date'), ), }),
        ('Vincitore', {'fields': (('winner', ), ), }),
        ('Partecipanti', {'fields': (('participants', ), ), }), )
    filter_horizontal = ('participants', )
    readonly_fields = ('id', 'date')
    ordering = ['-date']

    def get_participants(self, model):
        return ", ".join([str(participant) for participant in model.participants.all()])
    get_participants.short_description = 'Partecipanti'
