# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0013_auto_20171126_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='iron_required',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='building',
            name='wood_required',
            field=models.IntegerField(default=10),
        ),
    ]
