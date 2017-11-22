# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile, Belongings
# Create your views here.

def user_login(request):
    if request.method == "POST":
	form = LoginForm(request.POST)
	if form.is_valid():
	    cd = form.cleaned_data
	    user = authenticate(username = cd["username"],
				password = cd["password"])
	    if user is not None:
		if user.is_active:
		    login(request, user)
		    profile = Profile.objects.get(user=user)
		    profile.count += 1
 		    profile.save()
		    messages.add_message(request, messages.INFO, "Logged in successfully")
		    return redirect("battle:central")
		else:
		    messages.add_message(request, messages.INFO, "The account is not active")
		    return redirect("account:user_login")
	    else:
                messages.add_message(request, messages.INFO, "Invalid Login")
		return redirect("account:user_login")
    else:
	form = LoginForm()
    return render(request, "account/login.html", {"form":form})


def register(request):
    if request.method == 'POST':
	user_form = UserRegistrationForm(request.POST)
	if user_form.is_valid():
	    new_user = user_form.save(commit=False)
	    new_user.set_password(user_form.cleaned_data['password'])
	    new_user.save()
	    valid_coordinates = False
	    while valid_coordinates == False:
	        coordinateX = random.randint(0,1)
	        coordinateY = random.randint(0,1)
	        profiles = Profile.objects.filter(coordinateX = coordinateX, coordinateY = coordinateY)
	        if not profiles:
		    valid_coordinates = True
	    	    profile = Profile.objects.create(user=new_user,
					count=0,
					tribe=user_form.cleaned_data["tribe"],
					coordinateX = coordinateX,
					coordinateY = coordinateY)
	            profile.save()
	            belongings = Belongings.objects.create(user = new_user,
                                                   gold = 500)
	            belongings.save()
		#if profiles are full, report with email
     
            # return render(request, 'account/register_done.html', {'new_user': new_user})
	    messages.add_message(request, messages.INFO, "You registered successfully and can now login")
	    return redirect("account:user_login")
    else:
	user_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_form": user_form})

@login_required
def dashboard(request):
    return HttpResponse("DASHBOARD")

@login_required
def edit(request):
    if request.method == "POST":
	user_form = UserEditForm(instance = request.user, data = request.POST)
	profile_form = ProfileEditForm(instance = request.user.profile, data = request.POST, files = request.FILES)
	if user_form.is_valid and profile_form.is_valid:
	    user_form.save()
	    profile_form.save()
    else:
	user_form = UserEditForm(instance = request.user)
	profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def user_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You successfully logged out")
    return redirect("account:user_login")
