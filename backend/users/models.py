from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=10,null=True,blank=True,unique=True)
    email=models.EmailField(null=True,blank=True,unique=True)
    profile_picture=models.ImageField(upload_to="profile_picture/",null=True,blank=True)
    bio=models.CharField(max_length=500,blank=True,null=True)
    

