# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length = 100)
    attack = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    time_required = models.IntegerField(default=10) # in seconds
    gold_required = models.IntegerField(default=10)
    description1 = models.TextField()
    description2 = models.TextField()

    def __str__(self):
	return "Unit {}".format(self.name)

class Building(models.Model):
    name = models.CharField(max_length = 100)
    time_required = models.IntegerField(default=10)
    gold_required = models.IntegerField(default=10)
    population = models.IntegerField(default = 1)#each building adds 1 to population
    description1 = models.TextField()
    description2 = models.TextField()

    def __str__(self):
	return "Building {}".format(self.name)

class Item(models.Model):
    name = models.CharField(max_length = 100)
    time_required = models.IntegerField(default = 0)
    gold_required = models.IntegerField(default = 0)
    description1 = models.TextField()
    description2 = models.TextField()

    def __str__(self):
	return "Item {}".format(self.name)

class BuildingInProgress(models.Model):
    building = models.ForeignKey(Building, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    added = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField(blank = True)

    def __str__(self):
	return "Building {} for User {}".format(self.building, self.user)

class Message(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='messages_received')
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, related_name = "messages_sent")
    subject = models.CharField(max_length = 100, blank = False)
    body = models.TextField(blank = True)
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('battle:message', args=[str(self.id)])

class Attack(models.Model):
    attacker = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='attacks_done')
    defender = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, related_name = "defences_done")
    warrior1 = models.IntegerField(default = 0)
    warrior2 = models.IntegerField(default = 0)
    warrior3 = models.IntegerField(default = 0)
    flag = models.IntegerField(default = 0)
    begin = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(blank = True)

