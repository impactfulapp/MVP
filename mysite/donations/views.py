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

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import *
from .forms import *

import psycopg2, pprint
from django.core.serializers import serialize


#get charity list from database
conn = psycopg2.connect(host="localhost", dbname="charity_db", user="postgres", password="postgres")
cur = conn.cursor()
getCommand = "SELECT name FROM all_charities"
cur.execute(getCommand)
all_charities = [str(x[0].encode('utf-8')) for x in cur.fetchall()]

#get charity details table from database
getCommand2 = "SELECT name, cause, rating, tagline FROM all_charities"
cur.execute(getCommand2)
database_details = cur.fetchall()
charity_details = {}
for item in database_details:
    charity_details[(str(item[0].encode('utf-8')))] = {}
    charity_details[(str(item[0].encode('utf-8')))]['cause'] = (str(item[1].encode('utf-8')))
    charity_details[(str(item[0].encode('utf-8')))]['rating'] = (item[2])
    try:
        charity_details[(str(item[0].encode('utf-8')))]['tagline'] = (str(item[3].encode('utf-8')))
    except Exception:
        charity_details[(str(item[0].encode('utf-8')))]['tagline'] = 'Unknown'        

@login_required
def index(request):
    #get list of cards
    donation_list = Donation.objects.filter(donation_donor=request.user).order_by('-donation_date')
    total_donations = get_total_donated(request.user)

    #send info to html
    context = {'donation_list': donation_list , 'total_donations': total_donations} 
    return render(request, 'donations/index2.html', context)

def add_form(request, donation_id):
    charity_to_add = request.GET.get('charity', None)
    amount_to_add = request.GET.get('amount', None)
    date_to_add = request.GET.get('date', None)
    print(charity_to_add)
    print(amount_to_add)
    print(date_to_add)


    #check if donation id already exists
    donation_to_update = Donation.objects.filter(id=donation_id).first()
    if donation_to_update:
        #update old
        donation_to_update.donation_charity.charity_name = charity_to_add
        try:
            donation_to_update.donation_charity.charity_cause = charity_details[charity_to_add]['cause']
            donation_to_update.donation_charity.charity_rating = charity_details[charity_to_add]['rating']
            donation_to_update.donation_charity.charity_tagline = charity_details[charity_to_add]['tagline']
        except Exception:
            donation_to_update.donation_charity.charity_cause = 'Unknown'
            donation_to_update.donation_charity.charity_rating = 0
            donation_to_update.donation_charity.charity_tagline = 'Unknown'
        donation_to_update.donation_amount = amount_to_add
        donation_to_update.donation_date = date_to_add
        donation_to_update.save()

        # card_to_update_queryset = Card.objects.filter(id=donation_id)
        # card_to_update = card_to_update_queryset.first()
        # card_to_update.card_donation = donation_to_update
        # card_to_update.card_charity.charity_name = charity_to_add
        # try:
        #     card_to_update.card_charity.charity_cause = charity_details[new_charity_name]['cause']
        #     card_to_update.card_charity.charity_rating = charity_details[new_charity_name]['rating']
        #     card_to_update.card_charity.charity_tagline = charity_details[new_charity_name]['tagline']
        # except Exception:
        #     card_to_update.card_charity.charity_cause = 'Unknown'
        #     card_to_update.card_charity.charity_rating = 0
        #     card_to_update.card_charity.charity_tagline = 'Unknown'

        # card_to_update.card_date = date_to_add
        # card_to_update.save()

        new_total = get_total_donated(request.user)
        data = {'new_total': new_total, 'charity': donation_to_update.donation_charity.charity_name, 'amount': donation_to_update.donation_amount, 'date':donation_to_update.donation_date, 'cause': donation_to_update.donation_charity.charity_cause, 'tagline': donation_to_update.donation_charity.charity_tagline} 
        #serialize('json', card_to_update_queryset.first(), use_natural_foreign_keys=True, use_natural_primary_keys=True)
        #pprint.pprint(data)
        return JsonResponse(data)
    else:
        #make new    
        new_charity_name = charity_to_add
        new_amount = amount_to_add
        new_date = date_to_add
        new_charity = Charity(charity_name=new_charity_name)
        
        try:
            new_charity.charity_cause = charity_details[new_charity_name]['cause']
            new_charity.charity_rating = charity_details[new_charity_name]['rating']
            new_charity.charity_tagline = charity_details[new_charity_name]['tagline']
        except Exception:
            new_charity.charity_cause = 'Unknown'
            new_charity.charity_rating = 0
            new_charity.charity_tagline = 'Unknown'

        new_charity.save()
        new_donation = Donation(donation_charity=new_charity, donation_amount=new_amount, donation_date=new_date)
        new_donation.donation_donor = request.user
        new_donation.save()
        # new_card = Card(card_charity=new_charity, card_donation=new_donation, card_date=new_date, card_user=request.user)
        # new_card.save()
        donation_list = Donation.objects.filter(donation_donor=request.user).order_by('-donation_date')
        
        return HttpResponse(200)
        #return HttpResponseRedirect('/donations/')
      

def get_charities(request):
    letters = str(request.GET.get('term', None))
    #print "Letters: ", letters
    some_charities = []
    for name in all_charities:
        if letters.lower() in name.lower():
            some_charities.append(name)
        if len(some_charities) == 10:
            break
    #pprint.pprint(some_charities)
    data = { 'charities': some_charities }
    return JsonResponse(data)

def get_total_donated(user):
    donation_list = Donation.objects.filter(donation_donor=user)
    total_donations = 0
    for item in donation_list:
        total_donations = total_donations + item.donation_amount
    return total_donations

def detail(request, donation_id):
    return HttpResponse("You're looking at donation %s." % donation_id)

def delete_update(request, donation_id):
    Donation.objects.filter(id=donation_id).first().delete()
    # donation_delete = get_object_or_404(Donation, pk=donation_id).delete()
    total_donations = get_total_donated(request.user)
    data = { 'total': total_donations }
    return JsonResponse(data)

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

    return render(request, 'donations/settings2.html', {
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
