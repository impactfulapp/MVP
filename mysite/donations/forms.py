#import floppyforms as forms
from django import forms

import psycopg2
from .models import *


class NewCardForm(forms.Form):
   new_charity = forms.CharField()
   new_amount = forms.CharField()
   new_date = forms.DateField()
"""
   #get charity list from database
   conn = psycopg2.connect(host="localhost", database="niravsuraiya")
   cur = conn.cursor()
   getCommand = "SELECT name FROM all_charities"
   cur.execute(getCommand)
   charity_list = cur.fetchall()
   print "Charity 1:" , charity_list[1]
   
   widgets = {
      'new_charity': forms.widgets.Input(datalist=charity_list)
      }


from django import forms
from .models import *

class NewCardForm(forms.Form):
   #new_charity = forms.CharField()
   new_amount = forms.CharField()
   new_date = forms.DateField()

class ListTextWidget(forms.TextInput):
   def __init__(self, data_list, name, *args, **kwargs):
      super(ListTextWidget, self).__init__(*args, **kwargs)
      self._name = name
      self._list = data_list
      self.attrs.update({'list':'list__%s' % self._name})

   def render(self, name, value, attrs=None):
      text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
      data_list = '<datalist id="list__%s">' %self._name
      for item in self._list:
         data_list += '<option value=%s">' % item
      data_list += '</datalist>'

      return (text_html + data_list)

class AddForm(forms.Form):
   new_charity = forms.CharField(required=True)

   def __init__(self, *args, **kwargs):
      _charity_list = kwargs.pop('data_list', None)
      super(AddForm, self).__init__(*args, **kwargs)
      self.fields['new_charity'].widget = ListTextWidget(data_list=_charity_list, name='charity-list')

"""
