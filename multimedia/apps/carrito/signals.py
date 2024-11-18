# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Carrito

User = get_user_model()


@receiver(post_save, sender=User)
def crear_carrito_usuario(sender, instance, created, **kwargs):
    if created:
        Carrito.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def guardar_carrito_usuario(sender, instance, **kwargs):
    instance.carrito.save()
