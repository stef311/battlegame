# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0012_attack'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='iron_required',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='unit',
            name='wood_required',
            field=models.IntegerField(default=10),
        ),
    ]
