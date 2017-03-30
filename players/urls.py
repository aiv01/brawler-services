from django.conf.urls import url
from players.views import PlayerAlreadyExistsView, PlayerRegisterView, PlayerPhotoView

urlpatterns = [
    url(r'^already-exists/$', PlayerAlreadyExistsView.as_view(), name='player_already_exists'),
    url(r'^register/$', PlayerRegisterView.as_view(), name='player_register'),
    url(r'^photo/$', PlayerPhotoView.as_view(), name='player_photo_audio'),
]
