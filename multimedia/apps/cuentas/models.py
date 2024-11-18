from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Cliente(AbstractUser):
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=5)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
