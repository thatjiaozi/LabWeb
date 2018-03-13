from django.contrib.admin import AdminSite
from django.contrib.auth.models import User

from .models import Products, Categories, Sales, Products_Categories, Sales_Products

class CustomAdminSite(AdminSite):
    site_header = 'Comercial Valmir'
    site_title = 'Comercial Valmir | Administracion'
    index_title = 'Administracion'


admin_site = CustomAdminSite(name='admin')

admin_site.register(User)
admin_site.register(Products)
admin_site.register(Categories)
admin_site.register(Sales)
admin_site.register(Products_Categories)
admin_site.register(Sales_Products)
