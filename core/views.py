from django.shortcuts import render
from core.models import *

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)