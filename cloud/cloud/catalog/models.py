from django.db import models

# Create your models here.
class Categoria(models.Model):
    Nombre = models.CharField(max_length = 40, blank=False, null=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ('Nombre',)
    def save(self):
        super(Categoria, self).save()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(str.encode('hello world'), ('127.0.0.1', 2103))

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

class Sales(models.Model):
    TotalPayment = models.DecimalField(max_digits = 10, decimal_places = 2)
    SaleDate = models.DateTimeField()

class Administrators(models.Model):
    Name = models.CharField(max_length = 40)
    PasswordHash = models.CharField(max_length = 40)

class Employees(models.Model):
    Name = models.CharField(max_length = 40)
    PasswordHash = models.CharField(max_length = 40)
    IDAdmin = models.ForeignKey(Administrators, on_delete=models.CASCADE)

class Products_Categories(models.Model):
    class Meta:
        unique_together = (('IDProduct', 'IDCategory'),)
    IDProduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    IDCategory = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Sales_Products(models.Model):
    class Meta:
        unique_together = (('IDSale', 'IDProduct'),)
    Quantity = models.IntegerField()
    IDSale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    IDProduct = models.ForeignKey(Products, on_delete=models.CASCADE)

