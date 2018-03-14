from django.db import models

# Create your models here.

class Categoria(models.Model):
    Nombre = models.CharField(max_length = 40, blank=False, null=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ('Nombre',)

class Producto(models.Model):
    Nombre = models.CharField(max_length = 40)
    Descripcion = models.CharField(max_length = 40, default = 'none')
    Precio = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    En_Existencia = models.IntegerField(default = 0)
    Categorias = models.ManyToManyField(Categoria)
    Codigo = models.CharField(max_length = 128)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ('Nombre',)

class Folio(models.Model):
    Fecha = models.DateTimeField()
    Productos = models.ManyToManyField(Producto, through='Venta')

    @property
    def Pago_Total(self):
        accum = 0
        for producto in self.Productos.all():
            accum += Venta.objects.get(folio=self.id, producto=producto.id).Cantidad * producto.Precio
        return accum

    def __str__(self):
        return 'Folio ' + str(self.id) + ': ' + '$' + str(self.Pago_Total) + ' MXN'

    class Meta:
        ordering = ('id',)

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    folio = models.ForeignKey(Folio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.producto) + ' - ' + str(self.folio)

    class Meta:
        ordering = ('id',)
