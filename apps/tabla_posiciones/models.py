from django.db import models

# Create your models here.
from apps.equipos.models import Equipos
class Tabla(models.Model):
    posicion = models.CharField(max_length=2)
    Equipos = models.ForeignKey(Equipos, null=True, blank=True, on_delete=models.CASCADE)
    juegos_jugados = models.CharField(max_length=3)
    juegos_ganados = models.CharField(max_length=3)
    juegos_empatados = models.CharField(max_length=3)
    juegos_perdidos = models.CharField(max_length=3)
    goles_anotados = models.CharField(max_length=2)
    goles_permitidos = models.CharField(max_length=2)
    diferencia_goles = models.CharField(max_length=2)
    puntos = models.CharField(max_length=3)
