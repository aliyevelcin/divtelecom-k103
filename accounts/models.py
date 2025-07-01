from django.db import models
from django.contrib.auth.models  import AbstractUser 

class User(AbstractUser):
    image = models.ImageField(upload_to='images',null=True,blank=True)
    bio = models.TextField()
 
function staircase(n) {
    for (let i = 1; i <= n; i++) {
        const spaces = ' '.repeat(n - i);
        const hashes = '#'.repeat(i);
        console.log(spaces + hashes);
    }
}