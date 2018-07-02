from django.db import models

# Create your models here.
from django.contrib import admin
from django.db import models

# Register your models here.
class SquareTest(models.Model):
    Number=models.IntegerField()
    SquareNumber=models.IntegerField()
