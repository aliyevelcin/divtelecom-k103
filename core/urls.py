from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:id>', product, name='product'),
    path('about/', about, name='about'),
    path('list/', list, name='list'),
]