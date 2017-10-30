# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TodoItem(models.Model):
    title = models.CahrField(max_length = 30)
    description = models.CharField()
    due_date = models.DateTimeField()
    urgency = models.CharField()
    status = models.CharField()
