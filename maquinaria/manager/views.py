from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from manager.models import *
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.core.exceptions import ObjectDoesNotExist
import logging

def index(request):
  anuncios = Anuncio.objects.all()
  if request.method == 'POST':
    usuario = request.POST['username'].lower()
    clave = request.POST['password']

    acceso = authenticate(username=usuario, password=clave)
    if acceso is not None:
      if acceso.is_active:
        login(request,acceso)
        return HttpResponseRedirect('/nueva_maquinaria')
      else:
        formulario = AuthenticationForm()
        error_login = "usuario o clave incorrecta"
        return render_to_response('index.html',{'formulario':formulario,'error_login':error_login}, context_instance=RequestContext(request))
    else:
      formulario = AuthenticationForm()
      error_login = "usuario o clave incorrecta"
      return render_to_response('index.html',{'formulario':formulario,'error_login':error_login}, context_instance=RequestContext(request))
  formulario = AuthenticationForm()
  return render_to_response('index.html',{'formulario':formulario,'anuncios':anuncios}, context_instance=RequestContext(request))

def nueva_maquinaria(request):
  return render_to_response('index.html', context_instance=RequestContext(request))
