from django.conf.urls import patterns, include, url

from ballots import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from decisions import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'decisions.views.home', name='home'),
    # url(r'^decisions/', include('decisions.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^ballots/', include('ballots.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)