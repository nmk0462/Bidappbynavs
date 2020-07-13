from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
  pass
class Listings(models.Model):
    title1=models.CharField(max_length=64)
    desc =models.CharField(max_length=6400)
    bid=models.IntegerField()
    cat = models.CharField(max_length=64)
    lnk = models.CharField(max_length=640000,null=True,blank=True)
    usrr=models.CharField(max_length=64)
    crt=models.DateTimeField(default=datetime.now)
class Bids(models.Model):
    bids=models.IntegerField()
    unm=models.CharField(max_length=64)
    title2=models.CharField(max_length=64)
class Comments(models.Model):
    usrs=models.CharField(max_length=64)
    cmnt=models.CharField(max_length=640)
    titl=models.CharField(max_length=64)
class Watchlist(models.Model):
    usrs1=models.CharField(max_length=64)
    titlee=models.CharField(max_length=64)
class Winners1(models.Model):
    userwin=models.CharField(max_length=64)
    tll=models.CharField(max_length=64)
    desc1 =models.CharField(max_length=6400)
    bidd1=models.IntegerField()
    cat1 = models.CharField(max_length=64)
    lnk1 = models.CharField(max_length=64000)
