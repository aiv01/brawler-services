# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_auto_20170504_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='players/audio/', verbose_name='Audio'),
        ),
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='players/photos/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='player',
            name='tagline',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tagline'),
        ),
        migrations.AlterField(
            model_name='player',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Token'),
        ),
    ]
