# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0003_unit_time_to_make'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time_required', models.IntegerField(default=10)),
                ('gold_required', models.IntegerField(default=10)),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time_required', models.IntegerField(default=0)),
                ('gold_required', models.IntegerField(default=0)),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='time_to_make',
            new_name='time_required',
        ),
        migrations.AddField(
            model_name='unit',
            name='gold_required',
            field=models.IntegerField(default=10),
        ),
    ]
