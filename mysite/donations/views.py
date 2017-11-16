# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime

# Create your views here.

from django.http import HttpResponseRedirect

from .models import *
from .forms import NewCardForm

def index(request):
    card_list = Card.objects.all().order_by('-card_date')
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
            new_card = Card(card_charity=new_charity, card_donation=new_donation, card_date=new_date)
            new_card.save()
            return HttpResponseRedirect('/donations/')
    else:
        form = NewCardForm()
    context = {'card_list': card_list}
    return render(request, 'donations/index.html', context)

def detail(request, donation_id):
    return HttpResponse("You're looking at donation %s." % donation_id)

def login(request):
    return render(request, 'donations/login.html')
