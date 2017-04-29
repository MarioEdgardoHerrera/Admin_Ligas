from django.db import models
from apps.jugadores.models import Jugadores
# Create your models here.
class Tarjetas(models.Model):
    tarjetas_amarillas = models.CharField(max_length=1)
    tarjetas_rojas = models.CharField(max_length=1)
    Jugadores = models.ForeignKey(Jugadores, null=True, blank=True, on_delete=models.CASCADE)