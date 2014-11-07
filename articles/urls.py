from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^$', views.show_articles, name='show articles'),
  url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
)