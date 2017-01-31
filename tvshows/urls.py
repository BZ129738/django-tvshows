from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.tvshow_list, name="tvshow_list"),
    url(r'^(?P<category_slug>[-\w]+)/$', views.tvshow_list, name='list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tvshow_details, name='tvshow_details'),
]
