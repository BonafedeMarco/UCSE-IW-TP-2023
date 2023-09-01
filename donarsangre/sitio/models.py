from django.db import models
from django.contrib.auth.models import User

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
