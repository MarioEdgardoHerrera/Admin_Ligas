from django.db import models
from apps.equipos.models import Equipos
# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=3)
    equipo = models.ForeignKey(Equipos, null=True, blank=True, on_delete=models.CASCADE)
