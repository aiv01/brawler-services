from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'brawler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls))
]

admin.site.site_title = 'Brawler'
admin.site.site_header = 'Brawler'
admin.site.index_title = 'Amministrazione - AIV'

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls))
    )
