import django
from catalog.models import Products, Categories, Sales, Administrators, Employees, Products_Categories, Sales_Products

"""
    Populate products
"""

vasos = Products(IDProduct='1', ProductName='Paquete vasos', Description='Paquete de 5 vasos de hielo seco', Price=50, Quantity=100)
vasos.save()

tupper = Products(IDProduct='2', ProductName='Tupper', Description='Tupper de plastico', Price=100, Quantity=30)
tupper.save()

tina = Products(IDProduct='3', ProductName='Tina', Description='Tina infantil', Price=150, Quantity=10)
tina.save()

"""
    Populate Categories
"""

cocina = Categories(IDCategory='1', CategoryName="Cocina")
cocina.save()

juguetes = Categories(IDCategory='2', CategoryName="Juguetes")
juguetes.save()

hogar = Categories(IDCategory='3', CategoryName="Hogar")
hogar.save()

escolares = Categories(IDCategory='4', CategoryName="Articulos escolares")
escolares.save()

"""
  Populate Sales
"""

first = Sales(IDSale='1', TotalPayment = 100, SaleDate = '2018-02-21 00:00:00')
first.save()

second = Sales(IDSale='2', TotalPayment = 200, SaleDate = '2018-02-22 00:00:00')
second.save()

third = Sales(IDSale='3', TotalPayment = 600, SaleDate = '2018-02-23 00:00:00')
third.save()

"""
    Populate products categories
"""
vasos_cocina = Products_Categories(IDProduct = vasos, IDCategory = cocina)
vasos_cocina.save()

tupper_cocina = Products_Categories(IDProduct = tupper, IDCategory = cocina)
tupper_cocina.save()

tupper_hogar = Products_Categories(IDProduct = tupper, IDCategory = hogar)
tupper_hogar.save()

tina_hogar = Products_Categories(IDProduct = tina, IDCategory = hogar)
tina_hogar.save()

tina_escolares = Products_Categories(IDProduct = tina, IDCategory = escolares)
tina_escolares.save()

"""
    Populate sales products
"""
first_vasos = Sales_Products(IDSale = first, IDProduct = vasos, Quantity = 2)
first_vasos.save()

second_tupper = Sales_Products(IDSale = second, IDProduct = tupper, Quantity = 2)
second_tupper.save()

third_vasos = Sales_Products(IDSale = third, IDProduct = vasos, Quantity = 1)
third_vasos.save()

third_tupper = Sales_Products(IDSale = third, IDProduct = tupper, Quantity = 1)
third_tupper.save()

third_tina = Sales_Products(IDSale = third, IDProduct = tina, Quantity = 1)
third_tina.save()

""" 
    Populate admins
"""

Jeff = Administrators(IDAdmin='1', Name = "Jefferson Gutierritos", PasswordHash= "lala")
Watts = Administrators(IDAdmin='2', Name = "Watts Humphrey", PasswordHash = "PSP")

Jeff.save()
Watts.save()

"""
    Populate Employees
"""

Santana = Employees(IDEmployee='1', Name = "Carlos Santana", PasswordHash="lolo", IDAdmin = Jeff)
Santana.save()

Toro = Employees(IDEmployee='2', Name="Pepe el Toro", PasswordHash="123", IDAdmin = Watts)
Toro.save()