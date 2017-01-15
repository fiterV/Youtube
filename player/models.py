from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=30)
    ip = models.CharField(max_length=15)
    avatar = models.FileField()

