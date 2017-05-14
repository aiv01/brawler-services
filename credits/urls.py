from django.conf.urls import url
from credits.views import CreditListView

urlpatterns = [
    url(r'^json/$', CreditListView.as_view(), name='credits_json'),
]
