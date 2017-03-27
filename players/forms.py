from django.forms import ModelForm, PasswordInput
from players.models import Player


class PlayerAdminForm(ModelForm):
    model = Player
    fields = '__all__'

    class Meta:
        widgets = {'password': PasswordInput(), }
