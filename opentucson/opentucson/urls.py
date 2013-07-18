from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^api/v1/crimes/', include('crime.urls'), name='home'),
    # url(r'^opentucson/', include('opentucson.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
