from django.db import models
from datetime import date
import sys
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    year = models.IntegerField(validators=[MinValueValidator(1800),MaxValueValidator(2099)], default=2000)

class Shoe(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    size = models.IntegerField(default=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)