from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    about = models.CharField(max_length=100)
    pro1 = models.CharField(max_length=100)
    pd1 = models.CharField(max_length=70)
    pro2 = models.CharField(max_length=100)
    pd2 = models.CharField(max_length=70)
    pro3 = models.CharField(max_length=100)
    pd3 = models.CharField(max_length=70)
    ach1 = models.CharField(max_length=100)
    ad1 = models.CharField(max_length=70)
    ach2 = models.CharField(max_length=100)
    ad2 = models.CharField(max_length=70)
    ach3 = models.CharField(max_length=100)
    ad3 = models.CharField(max_length=70)
    adress = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    about = models.CharField(max_length=100)
    email = models.CharField(max_length=100)