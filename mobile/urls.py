from django.conf.urls import url
from mobile.views import MobileMatchParticipants, MobileMatchAudio

urlpatterns = [
    url(r'^match/participants/$', MobileMatchParticipants.as_view(), name='mobile_match_participants'),
    url(r'^match/audio/$', MobileMatchAudio.as_view(), name='mobile_match_audio'),
]
