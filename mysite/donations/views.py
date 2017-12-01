# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from social_django.models import UserSocialAuth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
import datetime

# Create your views here.

from django.http import HttpResponseRedirect

from .models import *
from .forms import NewCardForm

@login_required
def index(request):
    card_list = Card.objects.filter(card_user=request.user).order_by('-card_date')
    new_charity_name = ""
    new_amount = "" 
     
    if request.method == 'POST':
        form = NewCardForm(data=request.POST)
        if form.is_valid():
            new_charity_name = form.cleaned_data['new_charity']
            new_amount = form.cleaned_data['new_amount']
            new_date = form.cleaned_data['new_date']
            new_charity = Charity(charity_name=new_charity_name)
            new_charity.save()
            new_donation = Donation(donation_charity=new_charity, donation_amount=new_amount, donation_date=new_date)
            new_donation.save()
            new_card = Card(card_charity=new_charity, card_donation=new_donation, card_date=new_date, card_user=request.user)
            new_card.save()
            return HttpResponseRedirect('/donations/')
    else:
        form = NewCardForm()
    context = {'card_list': card_list}
    return render(request, 'donations/index.html', context)

def detail(request, donation_id):
    return HttpResponse("You're looking at donation %s." % donation_id)

#@login_required
def login(request):
    return render(request, 'donations/login.html')


@login_required
def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None
    """
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        google_login = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        google_login = None
    """

    return render(request, 'donations/settings.html', {
        'facebook_login': facebook_login,
        #'twitter_login': twitter_login,
        #'google_login': google_login
        #'can_disconnect': can_disconnect
        })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'donations/password.html', {'form': form})
