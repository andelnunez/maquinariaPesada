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

class AnuncioForm(forms.Form):
    tipo_choices = (
        ('alquilar', 'Alquilar'),
        ('vender', 'Vender'),
    )
    modelo = forms.CharField(max_length=100)
    tipo_anuncio = forms.ChoiceField(choices=tipo_choices)
    marca = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    tipo_maquinaria = forms.CharField(max_length=50)

class ClasificadoForm(forms.Form):
    tipo_choices = (
        ('servicio','Servicio'),
        ('repuesto','Repuesto'),
        ('accesorio','Accesorio'),
    )
    tipo = forms.ChoiceField(choices=tipo_choices)
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    imagen = forms.ImageField()
