# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0007_buildinginprogress_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildinginprogress',
            name='finished',
            field=models.DateTimeField(blank=True),
        ),
    ]
