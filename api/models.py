from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50)

class Clinica(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='clinicas/')
    numero_telefono = models.CharField(max_length=15)

class Doctor(models.Model):
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='doctores/')
    horarios = models.JSONField()  # [{'hora': '09:00', 'fecha': '2024-10-21', 'precio': 100}]

class Favorito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Cita(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    horario = models.JSONField()  # {'hora': '09:00', 'fecha': '2024-10-21'}
