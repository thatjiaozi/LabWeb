from django.db import models

# Create your models here.

class Administrador(models.Model):
    username = models.CharField(max_length = 40)
    password_hash = models.CharField(max_length = 40)
    full_name = models.CharField(max_length = 40)

class Empleados(models.Model):
    password_hash = models.CharField(max_length = 40)
    username = models.CharField(max_length = 40)
    full_name = models.CharField(max_length = 40)
    IDAdmin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
