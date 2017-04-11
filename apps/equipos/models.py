from django.db import models

# Create your models here.

class Equipos(models.Model):
    nombre = models.CharField(max_length=50)
    