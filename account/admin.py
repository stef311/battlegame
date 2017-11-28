# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Belongings

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user","date_of_birth","avatar"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Belongings)
