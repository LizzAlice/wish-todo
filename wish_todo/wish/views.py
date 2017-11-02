# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Wish


def wish_detail(request, pk):
    wish = get_object_or_404(Wish, pk = pk)
    return render(request, 'wish/detail.html', {'wish' : wish})
def wish_delete(request, pk):
    return HttpResponse('Delete-View für wishes')
def wish_edit(request, pk):
    return HttpResponse('Edit-view for wishes')
def wish_list(request):
    wish_set = Wish.objects.order_by('priority')
    return render(request, 'wish/list.html', {'wish_set' : wish_set})
def wish_add(request):
    return HttpResponse("wish add view")
