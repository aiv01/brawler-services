from django.conf.urls import url
from match.views import StartMatchView, AddPlayerToMatchView, EndMatchView

urlpatterns = [
    url(r'^start/$', StartMatchView.as_view(), name='start_match'),
    url(r'^add-player/$', AddPlayerToMatchView.as_view(), name='add_player_to_match'),
    url(r'^end/$', EndMatchView.as_view(), name='end_match'),
]
