from django.contrib import admin

from .models import *

admin.site.register({Product, ProductVersion, Color, Storage, Image, ColorImage,Color,Category,Faq})
# Register your models here.
