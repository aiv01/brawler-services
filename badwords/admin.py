from django.contrib import admin
from badwords.models import Badword


@admin.register(Badword)
class BadwordAdmin(admin.ModelAdmin):
    list_display = ('word', 'player')
    search_fields = ('word', 'player')
    list_filter = (('player', admin.RelatedOnlyFieldListFilter), )
    fieldsets = (
        ('Badword', {'fields': (('word', 'player'), )}, ), )
    readonly_fields = ('player', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'player', None) is None:
            obj.player = request.user
        obj.save()
