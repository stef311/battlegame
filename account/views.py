# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
		    return redirect("battle:central")
		else:
		    return HttpResponse("Disabled Account")
	    else:
		return HttpResponse("Invalid Login")
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
	    coordinateX = random.randint(-10,10)
	    coordinateY = random.randint(-10,10)
	    profile = Profile.objects.create(user=new_user,
					count=0,
					tribe=user_form.cleaned_data["tribe"],
					coordinateX = coordinateX,
					coordinateY = coordinateY)
	    profile.save()
	    belongings = Belongings.objects.create(user = new_user,
                                                   gold = 500)
	    belongings.save()
             
            # return render(request, 'account/register_done.html', {'new_user': new_user})
	    return redirect("account:dashboard")
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
    return redirect("account:user_login")
