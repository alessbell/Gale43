from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from articles import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'G43_tech_exercise.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'articles.views.index'),
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
