# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20171123_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='belongings',
            name='iron',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='belongings',
            name='wood',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='population',
            field=models.IntegerField(default=0),
        ),
    ]
