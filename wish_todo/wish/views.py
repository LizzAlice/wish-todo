# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def wish_detail(request):
    return HttpResponse("Hier werden mal wish-details stehen!")
def wish_delete(request):
    return HttpResponse('Delete-View für wishes')
def wish_edit(request):
    return HttpResponse('Edit-view for wishes')
def wish_list(request):
    return HttpResponse('list of all wishes; can be filtered')
def wish_add(request):
    return HttpResponse("wish add view")
