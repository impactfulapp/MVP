from django import forms
from .models import *

class NewCardForm(forms.Form):
   new_charity = forms.CharField()
   new_amount = forms.CharField()
   new_date = forms.DateField()
