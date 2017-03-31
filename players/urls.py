from django.conf.urls import url
from players.views import PlayerAlreadyExistsView, PlayerRegisterView, PlayerLoginView, PlayerPhotoView

urlpatterns = [
    url(r'^already-exists/$', PlayerAlreadyExistsView.as_view(), name='player_already_exists'),
    url(r'^register/$', PlayerRegisterView.as_view(), name='player_register'),
    url(r'^login/$', PlayerLoginView.as_view(), name='player_login'),
    url(r'^photo/$', PlayerPhotoView.as_view(), name='player_photo_audio'),
]
