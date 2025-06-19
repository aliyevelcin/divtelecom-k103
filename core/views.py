from django.shortcuts import render
from core.models import *

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)

def about(request):
    return render(request, 'about-us.html')


def list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'list.html', context)