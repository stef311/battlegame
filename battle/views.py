# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import sched
import time
from threading import Thread
import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BuyForm, TrainForm, MessageForm, AttackForm
from .models import Unit, Building, BuildingInProgress, Item, Message, Attack

from account.models import Belongings, Profile


# Create your views here.

def calculate_distance(user1, user2):
    user1X = user1.profile.coordinateX
    user1Y = user1.profile.coordinateY
    user2X = user2.profile.coordinateX
    user2Y = user2.profile.coordinateY

    #Manhattan
    distance = abs(user1X-user2X) + abs(user1Y-user2Y)
    print("distance: " + str(distance))
    return distance

def attack_player(user1, user2, time_required):
    print(time_required)
    time.sleep(time_required - 1)
    u1warrior1 = user1.belongings.warrior1

def level_up_building(user, building):
    time.sleep(building.time_required - 1)
    print(user)
    print(building)
    #belongings = Belongings.objects.get(user = user)
    if building.name == "market":
	user.belongings.market += 1
	print("market leveled up")
    	user.belongings.save()
    elif building.name == "army":
	user.belongings.army += 1
	print("army upgraded")
	user.belongings.save()

@login_required
def info(request):
    user = request.user
    user_tribe = user.profile.tribe
    context = {}
    context["tribe"] = user_tribe
    print(user_tribe)

@login_required
def buildings(request):
    user = request.user
    context = {}
    context["army"] = user.belongings.army
    context["market"] = user.belongings.market
    return render(request, "battle/buildings.html", context)

@login_required
def units(request):
    return HttpResponse("units")

@login_required
def items(request):
    return HttpResponse("items")

@login_required
def central(request):
    user = request.user
    context = {}
    context["user"] = user
    context["army"] = user.belongings.army
    context["market"] = user.belongings.market
    # h queue metavlhth exei ta items apo to BuildingInProgress model pou einai active
    now = datetime.datetime.now()
    buildings_in_queue = BuildingInProgress.objects.filter(user = user).filter(finished__gte=now)
    context["buildings_in_queue"] = buildings_in_queue
    attacks_in_queue = Attack.objects.filter(attacker = user).filter(end__gte=now)
    context["attacks_in_queue"] = attacks_in_queue
    context["units"] = {}
    context["units"]["warrior1"] = user.belongings.warrior1
    context["units"]["warrior2"] = user.belongings.warrior2
    context["units"]["warrior3"] = user.belongings.warrior3
    context["items"] = {}
    context["items"]["flag"] = user.belongings.flag

    if now.month == 11:
        month = "November"
    context["now"] = now
    context["month"] = month
    print(now.month)
    print "in queue" + str(buildings_in_queue)	
    return render(request, "battle/buildings/central.html", context)


#not needed. neither army function
@login_required
def market(request):
    user = request.user
    context = {}
    context["market"] = user.belongings.market
    print(user.belongings.market)
    if user.belongings.market > 0:
	if request.method == "POST":
	    form = BuyForm(request.POST)
	    if form.is_valid():
		cost = 0
		flag_count = form.cleaned_data["flag"] if form.cleaned_data["flag"] else 0
		flag_cost = Item.objects.get(name = "flag").gold_required
	 	cost += flag_count * flag_cost
		if user.belongings.gold >= cost:
		    user.belongings.gold -= cost
		    user.belongings.flag += flag_count
		    messages.add_message(request, messages.INFO, "Purchace complete")
		    return redirect("battle:central")
		else:
		    messages.add_message(request, messages.INFO, "Not enough gold")
		    return redirect("battle:central")
	    else:
                messages.add_message(request, messages.INFO, "The form is not valid")
                return redirect("battle:market")
	form = BuyForm()
	context["form"] = form
	return render(request, "battle/buildings/market.html", context)
    else:
        return HttpResponse("cannot do this")

def buy_items(request):
    user = request.user
    if request.method == "POST":
        form = BuyForm(request.POST)
        if form.is_valid():
   	    cost = 0
	    flag_count = form.cleaned_data["flag"]
	    flag_cost = Item.objects.get(name="flag").gold_required
            cost += flag_cost * flag_count
	    user.belongings.gold -= cost
	    user.belongings.save()
            return redirect('battle:central')
    else:
        form = BuyForm()
    items = Item.objects.all()
    print(items)
    user = request.user
    context = {}
    context["items"] = items
    context["market"] = user.belongings.market
    context["form"] = form
    if context["market"] > 0:
        return render(request, "battle/buildings/market/buy.html", context)
    else:
        return HttpResponse("cannot do this")

@login_required
def army(request):
    user = request.user
    context = {}
    context["army"] = user.belongings.army
    if user.belongings.army > 0 :
        if request.method == "POST":
            form = TrainForm(request.POST)
     	    if form.is_valid():
		cost = 0
		warrior1_count = form.cleaned_data["warrior1"] if form.cleaned_data["warrior1"] else 0
		warrior1_cost = Unit.objects.get(name="warrior1").gold_required
		cost += warrior1_count * warrior1_cost
		warrior2_count = form.cleaned_data["warrior2"] if form.cleaned_data["warrior2"] else 0
		warrior2_cost = Unit.objects.get(name="warrior2").gold_required
		cost += warrior2_count * warrior2_cost
		warrior3_count = form.cleaned_data["warrior3"] if form.cleaned_data["warrior3"] else 0
		warrior3_cost = Unit.objects.get(name="warrior3").gold_required
		cost += warrior3_count * warrior3_cost
		if user.belongings.gold >= cost:
		    user.belongings.gold -= cost
                    user.belongings.warrior1 += warrior1_count
                    user.belongings.warrior2 += warrior2_count
		    user.belongings.warrior3 += warrior3_count
		    user.belongings.save()
		    return redirect('battle:central')
	   	    	#na stelnw edw ena message( san to flash)
		else:
                    return HttpResponse("Not enough gold")
	    else:
		messages.add_message(request, messages.INFO, "The form is not valid")
		return redirect("battle:army")
	form = TrainForm()
	context["form"] = form
	return render(request, "battle/buildings/army.html", context)
    else:
	return HttpResponse("You do not have an army")

@login_required
def train_units(request):
    user = request.user
    if request.method == "POST":
        form = BuyForm(request.POST)
        if form.is_valid():
   	    cost = 0
	    warrior1_count = form.cleaned_data["warrior1"]
	    warrior1_cost = Item.objects.get(name="warrior1").gold_required
            cost += warrior1_count * warrior1_cost
	    user.belongings.gold -= cost
	    user.belongings.save()
            return redirect('battle:central')
    else:
        form = BuyForm()
    context = {}
    context["army"] = user.belongings.army
    if context["army"] > 0:
	return render(request, "battle/buildings/army/buy.html", context)
    else:
 	return HttpResponse("cannot do this")

@login_required
def upgrade_building(request, building_name):
    user = request.user
    context = {}
    print(building_name)
    building = Building.objects.get(name=building_name)
    if building:
	print "BUILDING!"
	name = building.name
	cost = building.gold_required
 	time = building.time_required
	desc1 = building.description1
	desc2 = building.description2

	context["building"] = building

    return render(request, "battle/buildings/build.html", context)

def print_hello(seconds):
    print "DOOOOOONE!!!!!!!!!!"
    time.sleep(seconds)
    print "AGAIN!!!!"

@login_required
def upgrade_building_done(request, building_name):
    user = request.user
    building = Building.objects.get(name=building_name)
    print(user.belongings.gold)
    if user.belongings.gold >= building.gold_required:
	user.belongings.gold -= building.gold_required
	user.belongings.save()
	time_required = building.time_required
	#na to ftiaksw na mh ksanaginetai na xtistei to idio ktirio
	#add in building_in_progress
	now = datetime.datetime.now()
	finished = now + datetime.timedelta(seconds=time_required)
	print(now)
	print "ready at "+str(finished)
	building_in_progress = BuildingInProgress.objects.create(building=building,user=user,finished=finished)
	building_in_progress.save()
        year = finished.year
        month = finished.month
	day = finished.day
	hour = finished.hour
	minutes = finished.minute
	seconds = finished.second

	
   	 
	
#Apparently, if you are using graphics, the code controlling the graphics must be in the main thread. Perhaps try starting the question thread before the timer thread? If you are using Python 3.4 or above, try assert threading.current_thread() == threading.main_thread() to check if one thread is the main thread. Also see this question and/or this question. – Matthew Jan 17 '16 at 18:45
#add a comment#s = sched.scheduler(time.time, time.sleep)
	#s.enterabs(datetime.datetime(year,month,day, hour, minutes, seconds).timestamp, 1, print_hello())
	#s.enterabs(datetime.datetime(year,month,day, hour, minutes, seconds+5) ,1, print_hello(),[])
	#s.run
	t1 = Thread(target = level_up_building, kwargs = {"user":user, "building":building})
        t1.start()        
        return redirect("battle:central")

	#panw h afairesh
    else:
	return HttpResponse("cannot do that")

@login_required
def players(request):
    user = request.user
    users = User.objects.all()
    context = {}
    context["user"] = user
    context["users"] = users
    return render(request,"battle/players.html",context)

@login_required
def player(request, username):
    player = User.objects.get(username=username)
    player = Profile.objects.get(user = player)
    context = {}
    context["player"] = player
    return render(request, "battle/player.html", context)

@login_required
def send_message(request, username):
    user = request.user
    player = User.objects.get(username = username)
    context = {}
    if request.method == "POST":
	form = MessageForm(request.POST)
	if form.is_valid():
	    recipient = form.cleaned_data["recipient"]
	    subject = form.cleaned_data["subject"]
	    body = form.cleaned_data["body"]
	    message = Message.objects.create(recipient = recipient, sender = user, subject = subject, body = body)
	    message.save()
	    return render(request, "battle/central.html", context)
	else:
	    return HttpResponse("form is not valid")
    else:
	form = MessageForm()
	context["form"] = form
	return render(request,"battle/send_message.html", context)

@login_required
def attack(request, username):
    user = request.user
    defender = User.objects.get(username = username)
    context = {}
    context["user2"] = defender
    if request.method == "POST":
	form = AttackForm(request.POST)
	if form.is_valid():
	    warrior1 = form.cleaned_data["warrior1"]
	    warrior2 = form.cleaned_data["warrior2"]
	    warrior3 = form.cleaned_data["warrior3"]
	    flag = form.cleaned_data["flag"]
	    now = datetime.datetime.now()
	    distance = calculate_distance(user, defender)
	    warrior1_speed = Unit.objects.get(name="warrior1").speed
	    warrior2_speed = Unit.objects.get(name="warrior2").speed
	    warrior3_speed = Unit.objects.get(name="warrior3").speed
	    smallest_speed = min(warrior1_speed, warrior2_speed, warrior3_speed)
            print("smallest speed: " + str(smallest_speed))
	    time_required = distance * smallest_speed
	    now = datetime.datetime.now()
	    finished = now + datetime.timedelta(seconds=time_required)
	    attack = Attack.objects.create(attacker = user, defender = defender, warrior1 = warrior1,\
					   warrior2 = warrior2, warrior3 = warrior3, begin = now, end = finished)
	    attack.save()
  	    attack_player(user, defender, time_required)

            attacks_in_queue = Attack.objects.filter(attacker = user).filter(end__gte=now)
	    return redirect("battle:central")
	else:
	    messages.add_message(request, messages.INFO, "The form is not valid")
	    return redirect("battle:army")
    else:
	form = AttackForm()
	context["form"] = form
	return render(request, "battle/attack.html", context)

@login_required
def all_messages(request):
	user = request.user
	context = {}
	context["user"] = user
	received_messages = Message.objects.filter(recipient = user)
	context["received"] = received_messages
 	sent_messages = Message.objects.filter(sender = user)
	context["sent"] = sent_messages
	return render(request, "battle/messages.html", context)

@login_required
def message(request,msg_id):
	user = request.user
	context = {}
	msg = Message.objects.get(id=msg_id)
	context["msg"] = msg
	return render(request,"battle/message.html", context)

@login_required
def send_message(request):
	user = request.user
	context = {}
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			recipient = form.cleaned_data["recipient"]
			subject = form.cleaned_data["subject"]
			body = form.cleaned_data["body"]
			msg = Message.objects.create(sender=user, recipient = recipient, subject = subject, body = body)
			msg.save()
			return redirect("battle:central")
		else:
			return HttpResponse("form is not valid")
	else:
		form = MessageForm()
		context["form"] = form
		return render(request, "battle/send_message.html", context)
@login_required
def sent_messages():
    pass

@login_required
def received_messages():
    passs
