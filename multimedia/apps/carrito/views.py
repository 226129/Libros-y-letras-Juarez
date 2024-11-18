# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.catalogo.models import Libro
from .models import Carrito


@login_required
def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    if libro not in carrito.libros.all():
        carrito.libros.add(libro)
        carrito.cantidad += 1
        carrito.calcular_subtotal()
        carrito.save()
    return redirect('carrito')


@login_required
def carrito_detalle(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    libros = carrito.libros.all()
    total = carrito.calcular_subtotal()

    context = {
        'carrito': carrito,
        'num_libros': carrito.libros.count(),
        'libros': libros,
        'total': total
    }
    return render(request, 'carrito.html', context)
