from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(default=datetime.now(), blank=None, null=None)
    country = models.CharField(max_length=50)