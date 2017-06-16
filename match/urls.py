from django.conf.urls import url
from match.views import AddRoomView, ResetRoomView, RoomListView, AddPlayerToRoomView, StartMatchView, EndMatchView

urlpatterns = [
    url(r'^add/$', AddRoomView.as_view(), name='add_room'),
    url(r'^reset/$', ResetRoomView.as_view(), name='reset_room'),
    url(r'^list/json/$', RoomListView.as_view(), name='room_list'),
    url(r'^add-player/$', AddPlayerToRoomView.as_view(), name='add_player_to_room'),
    url(r'^match/start/$', StartMatchView.as_view(), name='start_match'),
    url(r'^match/end/$', EndMatchView.as_view(), name='end_match'),
]
