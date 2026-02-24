from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre de tú héroe")
    raza = models.CharField(max_length=50, verbose_name="Raza")
    clase = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)
    vida = models.IntegerField(verbose_name="HP")
    fuerza = models.IntegerField(default=10)
    destreza = models.IntegerField(default=10)
    constitucion = models.IntegerField(default=10)
    inteligencia = models.IntegerField(default=10)
    sabiduria = models.IntegerField(default=10)
    carisma = models.IntegerField(default=10)
    inventario = models.IntegerField(default=10)

    def __str__(self):
     return f"{self.nombre} - Nivel {self.nivel} {self.clase}"

    def get_modificador(self, atributo):
     return (atributo - 10) // 2