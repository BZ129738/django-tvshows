from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.tvshow_list, name="tvshow_list"),
    url(r'^nota/$', views.tvshow_unaccepted, name="tvshow_unaccepted"),
    url(r'^articles/(?P<id>\d+)/$', views.article_details, name='article_details'),
    url(r'^articles/(?P<id>\d+)/delete/$', views.article_delete, name='article_delete'),
    url(r'^articles/(?P<id>\d+)/edit/$', views.article_update, name='article_update'),
    url(r'^articles/', views.article_list, name='article_list'),
    url(r'^newarticle/$', views.new_article, name='new_article'),
    url(r'^new/$', views.new_tvshow, name='new_tvshow'),
    url(r'^edit/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tvshow_update, name='tvshow_update'),
    url(r'^delete/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tvshow_delete, name='tvshow_delete'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.tvshow_list, name='list_by_category'),
    url(r'^(?P<id>\d+)/accept/$', views.tvshow_accept, name='tvshow_accept'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.tvshow_details, name='tvshow_details'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/comment/$', views.tvshow_comment, name='tvshow_comment'),
    url(r'^comment/(?P<id>\d+)/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^comment/(?P<id>\d+)/accept/$', views.comment_accept, name='comment_accept'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
