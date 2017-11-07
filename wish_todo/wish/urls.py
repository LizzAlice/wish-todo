from django.conf.urls import url

from . import views

app_name = 'wish'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.wish_detail, name = 'detail'),
    url(r'^(?P<pk>[0-9]+)/delete', views.wish_delete, name = 'delete'),
    url(r'^(?P<pk>[0-9]+)/edit', views.wish_edit, name = 'edit'),
    url(r'^list', views.wish_list, name = 'list'),
    url(r'^add', views.wish_add, name = 'add'),
]
