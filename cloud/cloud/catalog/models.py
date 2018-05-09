from django.db import models

# Create your models here.

class Categoria(models.Model):
    Nombre = models.CharField(max_length = 40, blank=False, null=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ('Nombre',)

class Producto(models.Model):
    Nombre = models.CharField(max_length = 70)
    Descripcion = models.CharField(max_length = 300, default = 'none')
    Imagen = models.CharField(max_length = 300, default = '')
    Precio = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    En_Existencia = models.IntegerField(default = 0)
    Categorias = models.ManyToManyField(Categoria)
    Codigo = models.CharField(max_length = 128)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ('Nombre',)
