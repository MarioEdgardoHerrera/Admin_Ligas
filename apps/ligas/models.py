from django.db import models

# Create your models here.
from apps.equipos.models import Equipos

class Liga(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    Equipos = models.ForeignKey(Equipos, null=True, blank=True, on_delete=models.CASCADE)
