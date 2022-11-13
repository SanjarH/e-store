from django.shortcuts import render
from django.views.generic.edit import CreateView

from products.models import Product

from .forms import ProductForm


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = '/products/'


    
def product_list_view(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products/product.html', context)