# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20171127_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='culture',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='science',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tribe',
            field=models.IntegerField(choices=[(b'1', b'Civilians'), (b'2', b'Barbarians')], default=1),
        ),
    ]