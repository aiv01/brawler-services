from django.conf.urls import url
from servers.views import ServerRegisterView, ServersJsonView

urlpatterns = [
    url(r'^register/$', ServerRegisterView.as_view(), name='server_register'),
    url(r'^json/$', ServersJsonView.as_view(), name='servers_json'),
]
