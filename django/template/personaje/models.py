import random

from django.db import models

RAZAS = [
    "Humano",
    "Elfo",
    "Enano",
    "Mediano",
    "Gnomo",
    "Semiorco",
    "Tiefling",
    "Dracónido",
]
CLASES = [
    "Bárbaro",
    "Bardo",
    "Clérigo",
    "Druida",
    "Explorador",
    "Guerrero",
    "Hechicero",
    "Mago",
    "Monje",
    "Paladín",
    "Pícaro",
    "Burjo",
]


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

    @staticmethod
    def roll_stat():
        """Tira 4d6, descarta el dado más bajo y devuelve la suma de los 3 restantes."""
        dados = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dados)[1:])

    def generate_stats(self):
        """Asigna raza y clase aleatorias y genera todas las estadísticas con roll_stat()."""
        self.raza = random.choice(RAZAS)
        self.clase = random.choice(CLASES)
        self.fuerza = self.roll_stat()
        self.destreza = self.roll_stat()
        self.constitucion = self.roll_stat()
        self.inteligencia = self.roll_stat()
        self.sabiduria = self.roll_stat()
        self.carisma = self.roll_stat()
        self.vida = max(
            1,
            (random.randint(1, 8) + self.get_modificador(self.constitucion))
            * self.nivel,
        )


class Character(models.Model):
    pass
