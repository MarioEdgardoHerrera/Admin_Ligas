from django.db import models

# Create your models here.
from apps.ligas.models import Liga
class Equipos(models.Model):
    nombre = models.CharField(max_length=50)
    Liga = models.ForeignKey(Liga, null=True, blank=True, on_delete=models.CASCADE)