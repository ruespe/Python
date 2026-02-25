from django import forms
from django.core.exceptions import ValidationError

from .models import Personaje

STAT_MIN = 1
STAT_MAX = 20


def stat_widget(label):
    return forms.NumberInput(
        attrs={
            "placeholder": f"1 - 20",
            "min": STAT_MIN,
            "max": STAT_MAX,
            "title": label,
        }
    )


class PersonajeForm(forms.ModelForm):
    AUTO_GENERATED_FIELDS = [
        "raza",
        "clase",
        "vida",
        "fuerza",
        "destreza",
        "constitucion",
        "inteligencia",
        "sabiduria",
        "carisma",
    ]

    auto_generar = forms.BooleanField(
        required=False,
        label="Generar estadísticas automáticamente (4d6)",
        widget=forms.CheckboxInput(),
        help_text="Si lo marcas, raza, clase y todos los stats se generarán aleatoriamente.",
    )

    class Meta:
        model = Personaje
        fields = [
            "nombre",
            "raza",
            "clase",
            "nivel",
            "vida",
            "fuerza",
            "destreza",
            "constitucion",
            "inteligencia",
            "sabiduria",
            "carisma",
            "inventario",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Ej: Arthas"}),
            "raza": forms.TextInput(attrs={"placeholder": "Ej: Humano"}),
            "clase": forms.TextInput(attrs={"placeholder": "Ej: Paladín"}),
            "nivel": forms.NumberInput(
                attrs={"placeholder": "1 - 20", "min": 1, "max": 20}
            ),
            "vida": forms.NumberInput(
                attrs={"placeholder": "1 - 999", "min": 1, "max": 999}
            ),
            "fuerza": stat_widget("Fuerza"),
            "destreza": stat_widget("Destreza"),
            "constitucion": stat_widget("Constitución"),
            "inteligencia": stat_widget("Inteligencia"),
            "sabiduria": stat_widget("Sabiduría"),
            "carisma": stat_widget("Carisma"),
            "inventario": forms.NumberInput(
                attrs={"placeholder": "Slots de inventario", "min": 0, "max": 100}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.AUTO_GENERATED_FIELDS:
            self.fields[field_name].required = False

    def _auto(self):
        """Devuelve True si el usuario marcó el checkbox de generación automática."""
        return self.cleaned_data.get("auto_generar", False)

    def _validar_stat(self, campo):
        valor = self.cleaned_data.get(campo)
        if self._auto():
            return valor
        if valor is not None and not (STAT_MIN <= valor <= STAT_MAX):
            raise ValidationError(f"Debe estar entre {STAT_MIN} y {STAT_MAX}.")
        return valor

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("auto_generar"):
            for field_name in self.AUTO_GENERATED_FIELDS:
                if cleaned_data.get(field_name) in (None, ""):
                    self.add_error(
                        field_name, "Este campo es obligatorio en modo manual."
                    )
        return cleaned_data

    def clean_nivel(self):
        nivel = self.cleaned_data.get("nivel")
        if nivel is not None and not (1 <= nivel <= 20):
            raise ValidationError("El nivel debe estar entre 1 y 20.")
        return nivel

    def clean_vida(self):
        vida = self.cleaned_data.get("vida")
        if vida is not None and vida < 1:
            raise ValidationError("La vida debe ser al menos 1.")
        return vida

    def clean_inventario(self):
        inv = self.cleaned_data.get("inventario")
        if inv is not None and not (0 <= inv <= 100):
            raise ValidationError("El inventario debe estar entre 0 y 100 slots.")
        return inv

    def clean_fuerza(self):
        return self._validar_stat("fuerza")

    def clean_destreza(self):
        return self._validar_stat("destreza")

    def clean_constitucion(self):
        return self._validar_stat("constitucion")

    def clean_inteligencia(self):
        return self._validar_stat("inteligencia")

    def clean_sabiduria(self):
        return self._validar_stat("sabiduria")

    def clean_carisma(self):
        return self._validar_stat("carisma")
