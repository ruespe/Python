from django.db import models

class Mision(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel_recomendado = models.IntegerField()
    recompensa_oro = models.IntegerField()
    activa = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)