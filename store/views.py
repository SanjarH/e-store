from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request,'home.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)
