from django.shortcuts import render
from .models import Libro

# Create your views here.


def index(request):
    libros = Libro.objects.all()

    context = {
        'libros': libros
    }

    return render(request, 'index.html', context)
