from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator

"""
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    localidad = models.CharField(max_length=30)
    grupo = models.CharField(max_length=2)
    factorPositivo = models.BooleanField(default=True)
    estado = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pk} - {self.nombreCompleto()} ({self.tipoSangre()})"

    def nombreCompleto(self):
        return f"{self.apellido}, {self.nombre}"

    def tipoSangre(self):
        return f"{self.grupo.upper()}{'+' if self.factorPositivo else '-'}"


class Pedido(models.Model):
    receptor = models.ForeignKey(Usuario, on_delete = models.CASCADE, null = False, blank = False)
    litrosRequeridos = models.FloatField()
    localidad = models.CharField(max_length=30)
    centroMedico = models.CharField(max_length=50)
    fechaLimite = models.DateField()
    imagen = models.ImageField(upload_to="ImagenesPedidos", blank = True, null = True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fechaLimite} | {self.receptor.tipoSangre()} | {self.litrosRequeridos} L"

class Donacion(models.Model):
    donante = models.ForeignKey(Usuario, on_delete = models.CASCADE, null = False, blank = False)

    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE, null = False, blank = False)
    litrosDonados = models.FloatField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.fecha} - {self.litrosDonados} L - {self.donante.nombreCompleto}"

"""

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    blood_type = models.CharField(max_length=255, null=True, blank=True)


class Location(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class BloodType(models.Model):
    blood_type = models.CharField(max_length=4, blank=False, null=False)

    def __str__(self):
        return self.blood_type

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=True)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE, blank=False, null=False)
    liters_required = models.FloatField(default = 0, blank=False, null=False)
    photo = models.ImageField(upload_to="ImagenesPedidos/", blank = True, null = True)
    liters_donated = models.FloatField(default = 0, blank=False, null=False, max_length = liters_required)
    estado = models.IntegerField(default=0)
    latitud = models.CharField(max_length=50, default="-31.252606961483437", blank=False, null=False)
    longitud = models.CharField(max_length=50, default="-61.49176597595215", blank=False, null=False)

    def __str__(self):
        return f"{self.pk}:{self.title[:20]}"
