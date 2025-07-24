from django.shortcuts import render,redirect
from core.models import *
from core.forms import *
def home(request):
    products = Product.objects.order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductCommentForm(request.POST)
        comment = form.save()
        comment.user = request.user
        comment.product = Product.objects.get(id=id)
        comment.save()
        return redirect('core:product', id=id)
    form = ProductCommentForm()
    context = {
        'product': product,
        'form': form
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


