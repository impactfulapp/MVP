# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=500, blank=True)
    phone = models.TextField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='donations/static/donations/images/')#default='/static/donations/images/anonymous.png')
    location = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.user.username

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
    donation_donor = models.ForeignKey(Profile, on_delete=models.CASCADE, null='TRUE')
    #use donation_donor.donation_set.objects.all() for user's list of donations
    def __str__(self):
        return "Donation to " + self.donation_charity.charity_name

class Card(models.Model):
    card_charity = models.ForeignKey(Charity, on_delete=models.CASCADE, null='TRUE')
    card_donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null='TRUE')
    card_date = models.DateField(default=datetime.date.today)
    card_user = models.ForeignKey(User, null='TRUE')
    def __str__(self):
        return "Card for " + self.card_charity.charity_name
