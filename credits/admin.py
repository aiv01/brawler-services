from django.contrib import admin
from sortable.admin import PositionAdmin
from credits.models import Credit, Role


@admin.register(Credit)
class CreditAdmin(PositionAdmin):
    list_display = ('position', 'name', 'surname', 'get_roles')
    list_display_links = ('name', )
    search_fields = ('name', 'surname', 'roles')
    list_filter = ('roles', )
    fieldsets = (
        ('Nome e cognome', {'fields': (('name', 'surname'), ), }),
        ('Ruoli', {'fields': ('roles', ), }),
        ('Altre informazioni', {'fields': ('other_info', ), }), )
    filter_horizontal = ('roles', )

    def get_roles(self, model):
        return ", ".join([str(role) for role in model.roles.all()])
    get_roles.short_description = 'Ruoli'


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', )
    search_fields = ('role', )
    fieldsets = (('Ruolo', {'fields': ('role', ), }), )
