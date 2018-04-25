from django.contrib import admin
from .models import Categoria
from .models import Productos

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categoria)
