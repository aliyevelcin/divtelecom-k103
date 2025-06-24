from django.shortcuts import render
from django.views.generic import CreateView
from accounts.models import User
from django.urls import reverse_lazy
from accounts.forms import *
from django.contrib.auth.views import *


class RegisterView(CreateView):
    model = User  
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = 'accounts/login/'
