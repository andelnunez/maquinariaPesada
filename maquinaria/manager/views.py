from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from manager.models import *
from manager.forms import *
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.core.exceptions import ObjectDoesNotExist
import logging

def index(request):
    anuncios = Anuncio.objects.filter(aprobado=True)
    if request.method == 'POST':
        usuario = request.POST['username'].lower()
        clave = request.POST['password']

        acceso = authenticate(username=usuario, password=clave)
        if acceso is not None:
            if acceso.is_active:
                login(request,acceso)
                return HttpResponseRedirect('/nuevo_anuncio')
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

@login_required(login_url='/')
def nuevo_banner(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = BannersForm(request.POST,request.FILES)
        if formulario.is_valid():
            banner = formulario.cleaned_data['banner']
            nuevoBanner = Banner.objects.create(usuario=usuario,banner=banner)
            nuevoBanner.save()

            return HttpResponseRedirect('/nuevo_banner')
    formulario = BannersForm()
    return render_to_response('nuevo_banner.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def nuevo_anuncio(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = AnuncioForm(request.POST,request.FILES)
        if formulario.is_valid():
            modelo = formulario.cleaned_data['modelo']
            tipo_anuncio = formulario.cleaned_data['tipo_anuncio']
            descripcion = formulario.cleaned_data['descripcion']
            marca = formulario.cleaned_data['marca']
            tipo_maquinaria = formulario.cleaned_data['tipo_maquinaria']

            if tipo_anuncio == 'alquilar':
                alquiler = True
            else:
                alquiler = False

            #Buscar tipo de Maquinaria
            try:
                maquinaria = Maquinaria.objects.get(tipo=tipo_maquinaria)
            except:
                maquinaria = Maquinaria.objects.create(tipo=tipo_maquinaria)
                maquinaria.save()

            anuncio = Anuncio.objects.create(usuario=usuario,modelo=modelo,marca=marca,descripcion=descripcion,alquiler=alquiler,maquinaria=maquinaria)
            anuncio.save()

            # ManyToMany Imagenes de Anuncio

            return HttpResponseRedirect('/nuevo_anuncio')

    formulario = AnuncioForm()
    return render_to_response('nuevo_anuncio.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/')
def nuevo_clasificado(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = ClasificadoForm(request.POST,request.FILES)
        if formulario.is_valid():
            tipo = formulario.cleaned_data['tipo']
            titulo = formulario.cleaned_data['titulo']
            descripcion = formulario.cleaned_data['descripcion']
            imagen = formulario.cleaned_data['imagen']

            clasificado = Clasificados.objects.create(usuario=usuario,tipo=tipo,titulo=titulo,descripcion=descripcion,imagen=imagen)
            clasificado.save()

            return HttpResponseRedirect('/nuevo_clasificado')

    formulario = ClasificadoForm()
    return render_to_response('nuevo_clasificado.html',{'formulario':formulario},context_instance=RequestContext(request))

def revisar_anuncio(request):
    lista_anuncios = Anuncio.objects.filter(aprobado=False)
    if request.method == 'POST':
        aprobar_anuncio = request.POST.getlist('aprobar_anuncio')
        for aprobar in aprobar_anuncio:
            anuncio = Anuncio.objects.get(id=aprobar)
            anuncio.aprobado = True
            anuncio.save()
        return HttpResponseRedirect('/revisar_anuncio')
    return render_to_response('revisar_anuncio.html',{'lista_anuncios':lista_anuncios},context_instance=RequestContext(request))

def revisar_clasificado(request):
    lista_clasificados = Clasificados.objects.filter(aprobado=False)
    if request.method == 'POST':
        aprobar_clasificado = request.POST.getlist('aprobar_clasificado')
        for aprobar in aprobar_clasificado:
            clasificado = Clasificados.objects.get(id=aprobar)
            clasificado.aprobado = True
            clasificado.save()
        return HttpResponseRedirect('/revisar_clasificado')
    return render_to_response('revisar_clasificado.html',{'lista_clasificados':lista_clasificados},context_instance=RequestContext(request))

def clasificados(request):
    clasificados = Clasificados.objects.filter(aprobado=True)
    return render_to_response('clasificados.html',{'clasificados':clasificados},context_instance=RequestContext(request))