# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TodoItem(models.Model):

    URGENCY_CHOICES = (
        ('h', 'urgent'),
        ('m', 'moderately urgent'),
        ('l', 'not urgent')
    )

    STATUS_CHOICES = (
        ('done', 'done'),
        ('progress', 'in progress'),
        ('finished', 'finished')
    )

    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 300, blank = True)
    due_date = models.DateTimeField(blank = True)
    urgency = models.CharField(max_length = 20, choices = URGENCY_CHOICES)
    status = models.CharField(max_length = 30, choices = STATUS_CHOICES)

    class Meta:
        verbose_name = 'Todo Item'
    def __str__(self):
        return self.title
