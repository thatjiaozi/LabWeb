from django.contrib import admin
from .models import Categorias
from .models import Productos

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categorias)
