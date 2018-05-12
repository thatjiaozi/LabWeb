from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import models
from daterange_filter.filter import DateRangeFilter
from .models import Producto, Categoria, Venta, Folio, Reporte

class CustomAdminSite(AdminSite):
    site_header = 'Comercial Valmir'
    site_title = 'Comercial Valmir | Administracion'
    index_title = 'Administracion'


class ProductoModelAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Descripcion', 'Precio', 'En_Existencia',
                    'Codigo']
    list_editable = ['En_Existencia']
    list_filter = ['Categorias']
    search_fields = ['Nombre', 'Codigo']

    class Meta:
        model = Producto


class FolioModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Fecha', 'TicketFolio']
    list_filter = ['Fecha', ('Fecha', DateRangeFilter)]
    search_fields = ['id']

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.TicketFolio)

    show_firm_url.short_description = "Firm URL"

    class Meta:
        model = Folio

class ReporteModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'ReporteLink']
    search_fields = ['id']

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.ReporteLink)

    show_firm_url.short_description = "Firm URL"

    class Meta:
        model = Folio

class VentaModelAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'Cantidad']
    search_fields = ['folio__id']

    class Meta:
        model = Venta


admin_site = CustomAdminSite(name='admin')


class CategoriaModelAdmin(admin.ModelAdmin):
    search_fields = ['Nombre']

    class Meta:
        model = Categoria


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email',
                    'is_staff', 'is_active']

    def save_model(self, request, obj, form, change):
        # Override this to set the password to the value in the field if it's
        # changed.
        if obj.pk:
            orig_obj = models.User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()

    class Meta:
        model = User

class TickeAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'
 
admin_site = CustomAdminSite(name='admin')
admin_site.register(User, UserModelAdmin)
admin_site.register(Producto, ProductoModelAdmin)
admin_site.register(Categoria, CategoriaModelAdmin)
admin_site.register(Venta, VentaModelAdmin)
admin_site.register(Folio, FolioModelAdmin)
admin_site.register(Reporte, ReporteModelAdmin)