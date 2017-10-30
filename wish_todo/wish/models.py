# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime improt datetime

class Wish(models.Model):

    PRIORITY_CHOICES = (
        ('h','high'),
        ('m','medium'),
        ('l', 'low')
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length = 500, blank = True)
    date = models.DateTimeField(default = datetime.now)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True)
    priority = models.CharField(max_length = 10, choices = PRIORITY_CHOICES)
    image = models.ImageField(blank = True)
    link = models.URLField(blank = True)


    class Meta:
        verbose_name_plural = "Wishes"
    def __str__(self):
        return self.title
