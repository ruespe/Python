from django.core.management.base import BaseCommand
from cluedo.models import Arma, Habitacio, Personatge


class Command(BaseCommand):
    help = "Omple la base de dades amb les dades inicials del Cluedo"

    def handle(self, *args, **options):
        personatges = [
            ("Miss Scarlett", "Una jove elegant i misteriosa de caràcter fort"),
            ("Coronel Mostassa", "Un militar retirat amb fama de temperamental"),
            ("Senyora Blanca", "La majordoma de la mansió, discreta i eficient"),
            ("Reverend Verd", "Un home de confiança aparentment honrada"),
            ("Senyora Paó", "Una dama de l'alta societat amb molts secrets"),
            ("Professor Pruna", "Un científic excèntric amb molts enemics"),
        ]

        armes = [
            ("Canelobre", "Un pesant canelobre de bronze daurat"),
            ("Ganivet", "Un ganivet de cuina molt afilat"),
            ("Tub de Plom", "Un tub metàl·lic pesat i rovellat"),
            ("Revòlver", "Una pistola antiga de sis trets"),
            ("Corda", "Una corda llarga i resistent de cànem"),
            ("Clau Anglesa", "Una gran clau de metall de color negre"),
        ]

        habitacions = [
            ("Cuina", "On es preparen els àpats de la mansió"),
            ("Sala de Ball", "Un espai ampli decorat per als grans banquets"),
            ("Hivernacle", "Ple de plantes exòtiques i llum natural"),
            ("Menjador", "La sala principal de menjar amb gran taula"),
            (
                "Sala de Billar",
                "Amb una taula de billar al centre i trofeus a les parets",
            ),
            ("Biblioteca", "Milers de llibres cobreixen les parets de fusta"),
            ("Estudi", "El despatx privat del propietari amb molts papers"),
            ("Vestíbul", "L'entrada principal de la mansió amb gran escala"),
            ("Sala d'Estar", "Un lloc còmode amb sofàs i llar de foc"),
        ]

        creats = 0

        for nom, desc in personatges:
            _, created = Personatge.objects.get_or_create(
                nom=nom, defaults={"descripcio": desc}
            )
            if created:
                creats += 1
                self.stdout.write(f"  Creat personatge: {nom}")

        for nom, desc in armes:
            _, created = Arma.objects.get_or_create(
                nom=nom, defaults={"descripcio": desc}
            )
            if created:
                creats += 1
                self.stdout.write(f"  Creada arma: {nom}")

        for nom, desc in habitacions:
            _, created = Habitacio.objects.get_or_create(
                nom=nom, defaults={"descripcio": desc}
            )
            if created:
                creats += 1
                self.stdout.write(f"  Creada habitació: {nom}")

        if creats > 0:
            self.stdout.write(
                self.style.SUCCESS(f"\n✓ {creats} elements creats correctament!")
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "\nTots els elements ja existien. No s'ha creat res nou."
                )
            )
