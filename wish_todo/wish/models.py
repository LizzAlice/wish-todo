# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class wish(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length = 500)
    price = models.FloatField()
    priority = models.CharField(max_length = 20)
    image = models.ImageField()
    link = models.URLField()
