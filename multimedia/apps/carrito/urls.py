# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito_detalle, name='carrito_detalle'),
    path('carrito/agregar/<int:libro_id>/',
         views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:libro_id>/',
         views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('pago_exitoso/', views.pago_exitoso, name='pago_exitoso'),
]
