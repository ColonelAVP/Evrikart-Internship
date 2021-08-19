# Requirements
from django.db import models


# Create your models here.
class Store(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    banner = models.ImageField(upload_to='banner/', blank=True,default='banner/white.jpg')
    profile_pic = models.ImageField(upload_to='profile_img/', blank=True,default='profile_img/white.jpg')
    store_name = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length =50)
    state = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.store_name
