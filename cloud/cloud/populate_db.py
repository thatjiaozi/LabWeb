import django
from catalog.models import Products, Categories, Sales, Administrators, Employees, Products_Categories, Sales_Products


"""
    Populate Categories
"""

cocina = Categories(CategoryName="Cocina")
cocina.save()

juguetes = Categories(CategoryName="Juguetes")
juguetes.save()

hogar = Categories(CategoryName="Hogar")
hogar.save()

escolares = Categories(CategoryName="Articulos escolares")
escolares.save()

