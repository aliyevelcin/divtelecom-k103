from django.db import models
from django.contrib.auth.models  import AbstractUser 

class User(AbstractUser):
    image = models.ImageField(upload_to='images',null=True,blank=True)
    bio = models.TextField()
 
