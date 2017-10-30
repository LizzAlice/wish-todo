from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^detail', views.item_detail, name = 'todo-item-detail'),
    url(r'^delete', views.item_delete, name = 'todo-item-delete'),
    url(r'^edit', views.item_edit, name = 'todo-item-edit'),
    url(r'^list', views.item_list, name = 'todo-item-list'),
    url(r'^add', views.item_add, name = 'todo-item-add'),

]
