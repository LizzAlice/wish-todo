# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def item_detail(request, pk):
    return HttpResponse("Todolist item details")
def item_delete(request, pk):
    return HttpResponse("Todolist item delete view")
def item_edit(request, pk):
    return HttpResponse("todolist item edit view")
def item_list(request):
    return HttpResponse("todolist item list view")
def item_add(request):
    return HttpResponse("add an item view")
