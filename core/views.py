from django.shortcuts import render
from core.models import *

def home(request):
    
    return render(request, 'index.html')