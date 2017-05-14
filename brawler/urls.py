from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players/', include('players.urls')),
    url(r'^servers/', include('servers.urls')),
    url(r'^credits/', include('credits.urls')),
]

admin.site.site_title = 'Brawler'
admin.site.site_header = 'Brawler'
admin.site.index_title = 'Amministrazione - AIV'

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls))
    )
