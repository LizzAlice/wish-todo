# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import TodoItem

def item_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk = pk)
    return render(request, 'todo/detail.html', {'todo': todo})
def item_delete(request, pk):
    return HttpResponse("Todolist item delete view")
def item_edit(request, pk):
    return HttpResponse("todolist item edit view")
def item_list(request):
    item_set = TodoItem.objects.all().order_by('-due_date')
    context = {
        'item_set' : item_set
    }
    return render(request, 'todo/list.html', context)
def item_add(request):
    return HttpResponse("add an item view")
