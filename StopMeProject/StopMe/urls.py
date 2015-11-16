from django.conf.urls import patterns, url
from StopMe import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))