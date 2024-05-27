from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#All banquets--------------------------------------------------------------
class banquet(models.Model):
    name=models.CharField(max_length=100)
    rent=models.BigIntegerField()
    address=models.CharField(max_length=250)
    location=models.CharField(max_length=100)
    bimage1=models.ImageField(upload_to='images')
    bimage2=models.ImageField(upload_to='images')
    bimage3=models.ImageField(upload_to='images')
    rating=models.IntegerField()
    is_active=models.BooleanField(default=True, verbose_name="Available")
#Manager----------------------------------------------------------------
class manager(models.Model):
    name=models.CharField(max_length=100)
    number=models.BigIntegerField()
    banqid=models.ForeignKey(banquet,on_delete=models.CASCADE,db_column='bid')
    is_active=models.BooleanField(default=True, verbose_name="Available")
#All menus----------------------------------------------------------------
class menu(models.Model):
    name=models.CharField(max_length=100)
    package=models.IntegerField()
    is_active=models.BooleanField(default=True, verbose_name="Available")
#All dishes----------------------------------------------------------------
class dishes(models.Model):
    name=models.CharField(max_length=150)
    price=models.FloatField()
    mid=models.ForeignKey(menu,on_delete=models.CASCADE,db_column='mid')
    is_active=models.BooleanField(default=True, verbose_name="Available")
#BanquetRating--------------------------------------------------------------
class rating(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    is_active=models.BooleanField(default=True, verbose_name="Available")
#banqcart----Removed----------------------------------------------------------
class banqcart(models.Model):
    bid=models.ForeignKey(banquet,on_delete=models.CASCADE,db_column='bid')
    uid=models.ForeignKey(User, on_delete=models.CASCADE,db_column="uid")
    qty=models.IntegerField(default=1)
#menucart----Removed----------------------------------------------------------
class menucart(models.Model):
    mid=models.ForeignKey(menu,on_delete=models.CASCADE,db_column='mid')
    uid=models.ForeignKey(User, on_delete=models.CASCADE,db_column="uid")
    qty=models.IntegerField(default=1)

#cart--------------------------------------------------------------------------
class order(models.Model):
    order_id=models.CharField(max_length=50)
    mid=models.ForeignKey(menu,on_delete=models.CASCADE,db_column='mid',default=9)
    bid=models.ForeignKey(banquet,on_delete=models.CASCADE,db_column='bid',default=9)
    uid=models.ForeignKey(User, on_delete=models.CASCADE,db_column="uid")
    qty=models.IntegerField(default=1)

#bookingcart--------------------------------------------------------------------------
class bkcart(models.Model):
    order_id=models.CharField(max_length=50)
    mid=models.ForeignKey(menu,on_delete=models.CASCADE,db_column='mid',default=9)
    bid=models.ForeignKey(banquet,on_delete=models.CASCADE,db_column='bid',default=9)
    uid=models.ForeignKey(User, on_delete=models.CASCADE,db_column="uid")
    qty=models.IntegerField(default=1)

#Order--------------------------------------------------------------------------
class morder(models.Model):
    order_id=models.CharField(max_length=50)
    mid=models.ForeignKey(menu,on_delete=models.CASCADE,db_column='mid')
    bid=models.ForeignKey(banquet,on_delete=models.CASCADE,db_column='bid')
    uid=models.ForeignKey(User, on_delete=models.CASCADE,db_column="uid")
    qty=models.IntegerField(default=1)
    