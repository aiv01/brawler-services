from django.conf.urls import url
from players.views import PlayerAlreadyExistsView, PlayerPhotoAudioView, PlayerRegisterView, PlayerLoginView, PlayerServerAuthView, PlayerClientAuthView, PlayerPhotoView

urlpatterns = [
    url(r'^already-exists/$', PlayerAlreadyExistsView.as_view(), name='player_already_exists'),
    url(r'^photo-audio/$', PlayerPhotoAudioView.as_view(), name='player_photo_audio'),
    url(r'^register/$', PlayerRegisterView.as_view(), name='player_register'),
    url(r'^login/$', PlayerLoginView.as_view(), name='player_login'),
    url(r'^server-auth/$', PlayerServerAuthView.as_view(), name='player_server_auth'),
    url(r'^client-auth/$', PlayerClientAuthView.as_view(), name='player_client_auth'),
    url(r'^photo/$', PlayerPhotoView.as_view(), name='player_photo'),
]
