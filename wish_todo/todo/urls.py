from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.item_detail, name = 'item-detail'),
    url(r'^(?P<pk>[0-9]+)/delete', views.item_delete, name = 'item-delete'),
    url(r'^(?P<pk>[0-9]+)/edit', views.item_edit, name = 'item-edit'),
    url(r'^list', views.item_list, name = 'item-list'),
    url(r'^add', views.item_add, name = 'item-add'),

]
