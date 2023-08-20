from django.db import models
from django.contrib.auth.models import User

class Donante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    grupo = models.CharField(max_length=2)
    factorPositivo = models.BooleanField(default=True)

class Receptor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    grupo = models.CharField(max_length=2)
    factorPositivo = models.BooleanField(default=True)
    centroMedico = models.CharField(max_length=60)