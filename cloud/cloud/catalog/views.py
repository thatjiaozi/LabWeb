from django.shortcuts import render
from .models import Categories
from .models import Products
from .models import Products_Categories

# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalogo.html', {
        'all_categories': Categories.objects.all(),
        'all_products': Products.objects.all()
    })