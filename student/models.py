from django.db import models

class sinfoin(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=255)
# Create your models here.
class act(models.Model):
    name = models.CharField(max_length=50)