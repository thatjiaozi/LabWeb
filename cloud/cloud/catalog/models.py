from django.db import models

# Create your models here.
class Products(models.Model):
    ProductName = models.CharField(max_length = 40)
    Description = models.CharField(max_length = 40, default = 'none')
    Price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    Quantity = models.IntegerField(default = 0)

class Categories(models.Model):
    CategoryName = models.CharField(max_length = 40)

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
