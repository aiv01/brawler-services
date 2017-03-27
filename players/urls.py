from django.conf.urls import url
from players.views import PlayerAlreadyExistsView, PlayerRegisterView


urlpatterns = [
    url(r'^already-exists/$', PlayerAlreadyExistsView.as_view(), name='player_already_exists'),
    url(r'^register/$', PlayerRegisterView.as_view(), name='player_register'),
]
