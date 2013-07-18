from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from crime.views import CrimeList, CrimeDetail

urlpatterns = patterns('',
    url(r'^$', CrimeList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', CrimeList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
