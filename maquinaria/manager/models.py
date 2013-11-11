#encoding:utf-8
from django.db.models.fields.related import ManyToManyField
from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
  nombre = models.CharField(max_length=100)

class Estado(models.Model):
  nombre = models.CharField(max_length=100)
  pais = models.ForeignKey(Pais)

class Usuario(models.Model):
  usuario = models.ForeignKey(User)
  pais = models.ForeignKey(Pais)
  calle = models.CharField(max_length=100)
  telefono = models.IntegerField()

class Maquinaria(models.Model):
  tipo = models.CharField(max_length=100)

class Imagen(models.Model):
  imagen = models.ImageField(upload_to='carga')

class Anuncio(models.Model):
  usuario = models.ForeignKey(User)
  maquinaria = models.ForeignKey(Maquinaria)
  modelo = models.CharField(max_length=100)
  alquiler = models.BooleanField()     # Si es True es alquiler. Si es False es Venta
  marca = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=100)
  aprobado = models.BooleanField(default=False)
  imagen = models.ManyToManyField(Imagen)

class Banner(models.Model):
  usuario = models.ForeignKey(User)
  banner = models.ImageField(upload_to='carga')

class Clasificados(models.Model):
  usuario = models.ForeignKey(User)
  tipo = models.CharField(max_length=50)
  titulo = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=100)
  imagen = models.ImageField(upload_to='carga')
  aprobado = models.BooleanField(default=False)

