from django.contrib import admin
from .models import Categoria, Autor, Libro

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Libro)
