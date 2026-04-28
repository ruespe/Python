from django.db import models
from django.contrib.auth.models import User


class Personatge(models.Model):
    """Personatge sospitós del Cluedo."""

    nom = models.CharField(max_length=100)
    descripcio = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Personatge"
        verbose_name_plural = "Personatges"
        ordering = ["nom"]


class Arma(models.Model):
    """Arma del crim del Cluedo."""

    nom = models.CharField(max_length=100)
    descripcio = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Arma"
        verbose_name_plural = "Armes"
        ordering = ["nom"]


class Habitacio(models.Model):
    """Habitació de la mansió del Cluedo."""

    nom = models.CharField(max_length=100)
    descripcio = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Habitació"
        verbose_name_plural = "Habitacions"
        ordering = ["nom"]


class Solucio(models.Model):
    """Solució secreta d'una partida, única per usuari i sessió."""

    usuari = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solucions")
    personatge = models.ForeignKey(Personatge, on_delete=models.CASCADE)
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE)
    habitacio = models.ForeignKey(Habitacio, on_delete=models.CASCADE)
    creada_en = models.DateTimeField(auto_now_add=True)
    resolta = models.BooleanField(default=False)
    # Temps de resolució en segons (null si la partida no s'ha resolt)
    temps_resolucio = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Partida de {self.usuari.username} ({self.creada_en.strftime("%d/%m/%Y %H:%M")})'

    class Meta:
        verbose_name = "Solució"
        verbose_name_plural = "Solucions"
        ordering = ["-creada_en"]


class Intent(models.Model):
    """Registre d'un intent d'acusació dins d'una partida."""

    solucio = models.ForeignKey(
        Solucio, on_delete=models.CASCADE, related_name="intents"
    )
    personatge = models.ForeignKey(Personatge, on_delete=models.CASCADE)
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE)
    habitacio = models.ForeignKey(Habitacio, on_delete=models.CASCADE)
    # Resultat de cada element
    encert_personatge = models.BooleanField(default=False)
    encert_arma = models.BooleanField(default=False)
    encert_habitacio = models.BooleanField(default=False)
    # True si els tres elements són correctes
    correcte = models.BooleanField(default=False)
    creat_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        estat = "✓" if self.correcte else "✗"
        return f"Intent {estat} de {self.solucio.usuari.username}"

    class Meta:
        verbose_name = "Intent"
        verbose_name_plural = "Intents"
        ordering = ["creat_en"]
