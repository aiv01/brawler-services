from django.conf.urls import url
from players.views import (PlayerAlreadyExistsView, PlayerGetPhotoView, PlayerGetAudioView, PlayerRegisterView, PlayerLoginView,
                           PlayerServerAuthView, PlayerClientAuthView, PlayerPhotoView, PlayerAudioView)


urlpatterns = [
    url(r'^already-exists/$', PlayerAlreadyExistsView.as_view(), name='player_already_exists'),
    url(r'^get-photo/$', PlayerGetPhotoView.as_view(), name='player_get_photo'),
    url(r'^get-audio/$', PlayerGetAudioView.as_view(), name='player_get_audio'),
    url(r'^register/$', PlayerRegisterView.as_view(), name='player_register'),
    url(r'^login/$', PlayerLoginView.as_view(), name='player_login'),
    url(r'^server-auth/$', PlayerServerAuthView.as_view(), name='player_server_auth'),
    url(r'^client-auth/$', PlayerClientAuthView.as_view(), name='player_client_auth'),
    url(r'^photo/$', PlayerPhotoView.as_view(), name='player_photo'),
    url(r'^audio/$', PlayerAudioView.as_view(), name='player_audio'),
]
