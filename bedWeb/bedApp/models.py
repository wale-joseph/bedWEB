from django.db import models

# Create your models here.
class Table(models.Model):
    chrome = models.CharField(max_length=128)
    start = models.CharField(max_length=128)
    end = models.CharField(max_length=128)