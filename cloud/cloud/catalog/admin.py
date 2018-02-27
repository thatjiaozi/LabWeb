from django.contrib import admin
from .models import Products
from .models import Sales
from .models import Administrators
from .models import Employees
from .models import Products_Categories
from .models import Categories
from .models import Sales_Products

# Register your models here.
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(Administrators)
admin.site.register(Employees)
admin.site.register(Products_Categories)
admin.site.register(Categories)
admin.site.register(Sales_Products)