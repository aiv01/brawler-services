from django.conf.urls import url
from servers.views import ServerRegisterView


urlpatterns = [
    url(r'^register/$', ServerRegisterView.as_view(), name='server_register'),
]
