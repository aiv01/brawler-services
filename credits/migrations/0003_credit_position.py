# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0002_auto_20170514_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Posizione'),
        ),
    ]
