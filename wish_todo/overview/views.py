# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {}
    return render(request, 'overview/index.html', context)
