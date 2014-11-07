from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
  url(r'^(?P<article_id>\d+)/show_articles/$', views.show_articles, name='show_articles'),
)