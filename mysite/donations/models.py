# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#import User model form Profile app?
import datetime

# Create your models here.

class Charity(models.Model):
    charity_name = models.CharField(max_length=200, null='TRUE')
    #charity_tag_1 = models.CharField(max_length=200)
    def __str__(self):
        return self.charity_name

class Donation(models.Model):
    donation_charity = models.ForeignKey(Charity, on_delete=models.CASCADE, null='TRUE')
    donation_amount = models.IntegerField(default=0, null='TRUE')
    donation_date = models.DateField(default=datetime.date.today)
    #donation_impact = models.CharField(max_length=200)
    #donation_donor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "Donation to " + self.donation_charity.charity_name

class Card(models.Model):
    card_charity = models.ForeignKey(Charity, on_delete=models.CASCADE, null='TRUE')
    card_donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null='TRUE')
    card_date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return "Card for " + self.card_charity.charity_name

