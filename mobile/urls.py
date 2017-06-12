from django.conf.urls import url
from mobile.views import MobileMatchParticipants

urlpatterns = [
    url(r'^match/participants/$', MobileMatchParticipants.as_view(), name='mobile_match_participants'),
]
