# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 07:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wish',
            options={'verbose_name_plural': 'Wishes'},
        ),
        migrations.AddField(
            model_name='wish',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='wish',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='wish',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='wish',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wish',
            name='priority',
            field=models.CharField(choices=[('h', 'high'), ('m', 'medium'), ('l', 'low')], max_length=10),
        ),
    ]
