from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'
        ordering = ['-created']

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(
        upload_to='/images/libros', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['-created']

    def __str__(self):
        return self.nombre
