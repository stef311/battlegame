# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Unit, Building, Item, BuildingInProgress, Message, Attack

# Register your models here.
class UnitAdmin(admin.ModelAdmin):
    list_display = ["name", "attack", "defence", "speed", "time_required"]

class BuildingAdmin(admin.ModelAdmin):
    list_display = ["name", "time_required", "gold_required"]

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "time_required", "gold_required"]

class BuildingInProgressAdmin(admin.ModelAdmin):
    list_display = ["building", "user", "added", "finished"]

class MessageAdmin(admin.ModelAdmin):
    list_display = ["recipient", "sender", "subject", "body"]

class AttackAdmin(admin.ModelAdmin):
    list_display = ["attacker", "defender", "warrior1", "warrior2", "warrior3", "flag", "begin", "end"]

admin.site.register(Unit, UnitAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(BuildingInProgress, BuildingInProgressAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Attack, AttackAdmin)
