# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from choices import CHOICES

# Create your models here.

class Profile(models.Model):
    
    coordinateX = models.IntegerField()
    coordinateY = models.IntegerField()
    #tribe = models.CharField(max_length = 5, choices = CHOICES)
    tribe = models.IntegerField(choices = CHOICES, default = 1)

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank = True, null = True)
    avatar = models.ImageField(upload_to = "users/%Y/%m/%d", blank = True)
    count = models.IntegerField()
    description = models.TextField()
    population = models.IntegerField(default = 0)
    science = models.IntegerField(default = 0)
    culture = models.IntegerField(default = 0)
    

    def __str__(self):
	    return "Profile for user {}".format(self.user.username)

class Belongings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gold = models.IntegerField(default = 0)
    wood = models.IntegerField(default = 0)
    iron = models.IntegerField(default = 0)
    army = models.IntegerField(default = 0)
    market = models.IntegerField(default = 0)
    warehouse = models.IntegerField(default = 0)
    academy = models.IntegerField(default = 0)
    museum = models.IntegerField(default = 0)    
    warrior1 = models.IntegerField(default = 0)
    warrior2 = models.IntegerField(default = 0)
    warrior3 = models.IntegerField(default = 0)
    flag = models.IntegerField(default = 0)

    def __str__(self):
	    return "Belongings for user {}".format(self.user.username)
