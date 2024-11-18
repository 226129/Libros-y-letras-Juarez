from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito_detalle, name='carrito_detalle'),
    path('carrito/agregar/<int:libro_id>/',
         views.agregar_al_carrito, name='agregar_al_carrito'),
]
