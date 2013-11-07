#encoding:utf-8
import datetime
from django.forms import ModelForm
from django.db import models 
from django import forms
from django.contrib.auth.models import User
from manager.models import *
from django.contrib.admin.widgets import AdminDateWidget 
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple

class BannersForm(forms.Form):
  banner = forms.ImageField()

class MaquinariaForm(forms.Form):
  tipo = forms.CharField(max_length=50)

