from django.db import models

# Create your models here.
def name(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    Email_id = models.CharField(max_length=100)
    password = models.IntegerField()

