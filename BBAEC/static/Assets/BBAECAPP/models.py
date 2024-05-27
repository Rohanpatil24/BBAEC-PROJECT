from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class banquet(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    rent=models.FloatField()
    is_active=models.BooleanField(default=True, verbose_name="Available")
    bimage=models.ImageField(upload_to='images')
    bimage2=models.ImageField(upload_to='images')
    bimage3=models.ImageField(upload_to='images')

class menu(models.Model):
    name=models.CharField(max_length=150)
    package=models.IntegerField()
    is_active=models.BooleanField(default=True, verbose_name="Available")


class dishes(models.Model):
    name=models.CharField(max_length=150)
    price=models.FloatField()
    mid=models.ForeignKey(menu,on_delete=models.CASCADE,db_column='mid')
    is_active=models.BooleanField(default=True, verbose_name="Available")

class banquetmanager(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField()

class menucart(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    banqid=models.ForeignKey(banquet,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)

class foodcart(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    menuid=models.ForeignKey(menu,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User, on_delete=models.CASCADE,db_column="uid")
    bid=models.ForeignKey(banquet, on_delete=models.CASCADE,db_column="bid")
    mid=models.ForeignKey(menu, on_delete=models.CASCADE,db_column="mid")
    qty=models.IntegerField(default=1)