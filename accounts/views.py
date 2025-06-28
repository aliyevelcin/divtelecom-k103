from django.shortcuts import render
from django.views.generic import CreateView
from accounts.models import User
from django.urls import reverse_lazy
from accounts.forms import *

from django.contrib.auth.views import *

class RegisterView(CreateView):
    template_name = 'register.html'
    model = User
    form_class = RegisterForm
    success_url = '/accounts/login/'
   

class LoginUser(LoginView):
    template_name = 'login.html'
    success_url = '/'
    form_class = LoginForm
    model = User

def orders(request,id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request,'orders.html',context )