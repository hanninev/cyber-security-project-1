from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    general = models.TextField()
