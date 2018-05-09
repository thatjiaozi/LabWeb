from django.shortcuts import render
from .models import Categoria
from .models import Producto

# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalogo.html', {
        'all_categories': Categoria.objects.all(),
        'all_products': Producto.objects.all()
    })
