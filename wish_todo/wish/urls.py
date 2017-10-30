from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.wish_detail, name = 'wish-detail'),
    url(r'^(?P<pk>[0-9]+)/delete', views.wish_delete, name = 'wish-delete'),
    url(r'^(?P<pk>[0-9]+)/edit', views.wish_edit, name = 'wish-edit'),
    url(r'^list', views.wish_list, name = 'wish-list'),
    url(r'^add', views.wish_add, name = 'wish-add'),
]
