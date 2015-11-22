from django.conf.urls import patterns, url
from StopMe import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^map', views.map, name='map'),
    )