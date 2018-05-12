from django.shortcuts import render
from .models import Categoria
from .models import Producto


# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalogo.html', {
        'all_categories': Categoria.objects.all(),
        'all_products': Producto.objects.all()
    })

def filterSideBar(request):
    checkedCategories = request.GET.getlist('category')
    print(checkedCategories)
    priceFilter = request.GET['priceFilter']
    if checkedCategories:
        filteredProducts = Producto.objects.filter(Categorias__in=checkedCategories).filter(Precio__gt = priceFilter)
    else:
        filteredProducts = Producto.objects.all().filter(Precio__gt = priceFilter)

    return render(request, 'catalog/catalogo.html', {
        'all_categories': Categoria.objects.all(),
        'all_products': filteredProducts
    })

def search(request):
    name = request.GET['prodName']
    if name:
        filteredProducts = Producto.objects.all().filter(Nombre__startswith = name)
    else:
        filteredProducts = Producto.objects.all()

    return render(request, 'catalog/catalogo.html', {
        'all_categories': Categoria.objects.all(),
        'all_products': filteredProducts
    })
