from django.shortcuts import render
from products.models import Product


    
def product_list_view(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products/product.html', context)