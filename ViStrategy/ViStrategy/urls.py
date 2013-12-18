from django.conf.urls import patterns, include, url
from testViStrategyDB.views import slide_window

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ViStrategy.views.home', name='home'),
    # url(r'^ViStrategy/', include('ViStrategy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^slide/(\w+)$', slide_window),
    # url(r'^polls/', include('polls.urls')),

    url(r'^testViStrategyDB/', include('testViStrategyDB.urls')),
)
