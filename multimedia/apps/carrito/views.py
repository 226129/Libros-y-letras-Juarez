# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.catalogo.models import Libro
from .models import Carrito, Pago


@login_required
def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    if libro not in carrito.libros.all():
        carrito.libros.add(libro)
        carrito.cantidad += 1
        carrito.calcular_subtotal()
        carrito.save()
    return redirect('carrito_detalle')


@login_required
def eliminar_del_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    if libro in carrito.libros.all():
        carrito.libros.remove(libro)
        carrito.cantidad -= 1
        carrito.calcular_subtotal()
        carrito.save()
    return redirect('carrito_detalle')


@login_required
def carrito_detalle(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    libros = carrito.libros.all()
    total = carrito.calcular_subtotal()

    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        paymentMethod = request.POST.get('paymentMethod')
        ccName = request.POST.get('ccName')
        ccNumber = request.POST.get('ccNumber')
        ccExpiration = request.POST.get('ccExpiration')
        ccCVV = request.POST.get('ccCVV')

        pago = Pago.objects.create(
            nombre=firstName,
            apellido=lastName,
            direccion=address,
            direccion2=address2,
            pais=country,
            estado=state,
            codigo_postal=zip_code,
            metodo_pago=paymentMethod,
            nombre_en_tarjeta=ccName,
            numero_tarjeta=ccNumber,
            expiracion=ccExpiration,
            cvv=ccCVV,
            total_a_pagar=total
        )
        carrito.libros.clear()
        return redirect('pago_exitoso')

    context = {
        'carrito': carrito,
        'num_libros': carrito.libros.count(),
        'libros': libros,
        'total': total
    }
    return render(request, 'carrito.html', context)


@login_required
def pago_exitoso(request):
    return render(request, 'pago_exitoso.html')
