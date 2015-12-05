from django.conf.urls import include, url
from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^bootstrap/$', views.indexb, name='indexb'),
    url(r'^list/$', views.list, name='list'),
	url(r'^bootstrap/list/$', views.listb, name='listb'),
    url(r'^rating/(?P<value>[0-9])/$', views.rating, name='rating'),
    url(r'^bootstrap/rating/(?P<value>[0-9])/$', views.ratingb, name='ratingb'),
    url(r'^bootstrap/(?P<name>.+)/$', views.detailb, name='detailb'),
    url(r'^(?P<name>.+)/$', views.detail, name='detail'),
]
