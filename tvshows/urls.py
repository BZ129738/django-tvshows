from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.tvshow_list, name="tvshow_list"),
    url(r'^new/$', views.new_tvshow, name='new_tvshow'),
    url(r'^edit/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tvshow_update, name='tvshow_update'),
    url(r'^delete/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tvshow_delete, name='tvshow_delete'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.tvshow_list, name='list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tvshow_details, name='tvshow_details'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)