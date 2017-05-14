from django.conf.urls import url
from credits.views import CreditJsonView

urlpatterns = [
    url(r'^json/$', CreditJsonView.as_view(), name='credits_json'),
]
