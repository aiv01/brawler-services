# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_auto_20170512_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude'),
        ),
    ]
