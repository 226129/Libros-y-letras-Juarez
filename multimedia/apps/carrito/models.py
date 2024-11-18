# models.py
from django.db import models
from apps.catalogo.models import Libro
from django.contrib.auth import get_user_model

User = get_user_model()


class Carrito(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='carrito')
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    libros = models.ManyToManyField(Libro, related_name='carritos')

    def calcular_subtotal(self):
        self.subtotal = sum(libro.precio for libro in self.libros.all())
        return self.subtotal

    def __str__(self):
        return f"Carrito de {self.usuario.username}"


class Pago(models.Model):
    metodos_pago = {
        ('Tarjeta de credito', 'Tarjeta de credito'),
        ('Tarjeta de debito', 'Tarjeta de debito'),
    }

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    direccion2 = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=100)
    metodo_pago = models.CharField(choices=metodos_pago, max_length=100)
    nombre_en_tarjeta = models.CharField(max_length=100)
    numero_tarjeta = models.CharField(max_length=16)
    expiracion = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    total_a_pagar = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Pago de {self.nombre} {self.apellido}"
