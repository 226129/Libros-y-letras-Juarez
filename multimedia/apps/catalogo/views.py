from django.shortcuts import render, redirect
from .models import Libro
from apps.cuentas.models import Cliente
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    query = request.GET.get('q')

    if query:
        libros = Libro.objects.filter(nombre__icontains=query)
    else:
        libros = Libro.objects.all()

    context = {
        'libros': libros
    }

    return render(request, 'index.html', context)


def ayuda(request):
    return render(request, 'ayuda.html')


@login_required
def perfil(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.telefono = request.POST.get('telefono')
        user.direccion = request.POST.get('direccion')
        user.ciudad = request.POST.get('ciudad')
        user.estado = request.POST.get('estado')
        user.pais = request.POST.get('pais')
        user.codigo_postal = request.POST.get('codigo_postal')
        user.save()
        messages.success(request, 'Perfil actualizado exitosamente')
        return redirect('perfil')
    return render(request, 'perfil.html')
