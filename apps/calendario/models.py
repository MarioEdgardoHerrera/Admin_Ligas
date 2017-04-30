from django.db import models

# Create your models here.
from apps.calendario.models import Calendario
class Calendario(models.Model):
    nombre = models.CharField(max_length=50)
    Equipos = models.ForeignKey(Equipos, null=True, blank=True, on_delete=models.CASCADE)

