from django.db import models

# Create your models here.

class Solicitud(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=300)
    fecha = models.DateTimeField()