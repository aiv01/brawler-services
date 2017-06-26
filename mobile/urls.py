from django.conf.urls import url
from mobile.views import MobileMatchParticipants, MobileMatchSendEmpower, MobileMatchSendMessage, MobileMatchAudio

urlpatterns = [
    url(r'^match/participants/$', MobileMatchParticipants.as_view(), name='mobile_match_participants'),
    url(r'^match/send-empower/$', MobileMatchSendEmpower.as_view(), name='mobile_match_send_empower'),
    url(r'^match/send-message/$', MobileMatchSendMessage.as_view(), name='mobile_match_send_message'),
    url(r'^match/audio/$', MobileMatchAudio.as_view(), name='mobile_match_audio'),
]
