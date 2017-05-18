from django.conf.urls import url
from badwords.views import BadwordJsonView

urlpatterns = [
    url(r'^json/$', BadwordJsonView.as_view(), name='badwords_json'),
]
