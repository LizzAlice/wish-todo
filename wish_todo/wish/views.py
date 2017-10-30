# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def wish_detail(request, pk):
    return HttpResponse("Details of question %s." % pk)
def wish_delete(request, pk):
    return HttpResponse('Delete-View für wishes')
def wish_edit(request, pk):
    return HttpResponse('Edit-view for wishes')
def wish_list(request):
    wish_set = Wish.objects.order_by()
    return HttpResponse('list of all wishes; can be filtered')
def wish_add(request):
    return HttpResponse("wish add view")
