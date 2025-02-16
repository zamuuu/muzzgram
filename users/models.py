from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class customUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=160)
    bio = models.TextField(blank=True, null=True, max_length=350)
    profile_pic = models.ImageField(
        upload_to='static/profile_pics/', 
        blank=True, 
        null='True',
        default="static/profile_pics/default_pp.jpg"
        )
    
    def __str__(self):
        return self.username

