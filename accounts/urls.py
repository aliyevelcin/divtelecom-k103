from django.urls import path
from accounts.views import *

from django.contrib.auth.views import LogoutView
app_name = 'accounts'

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
     path('orders/<int:id>', orders, name='orders'),
]