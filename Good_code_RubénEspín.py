# Comento el import os, sys, math que no es usado para nada
# import os, sys, math

# Comento el import math que no es usado para nada
# from math import *

# Comento el import json que no es usado para nada
# import json

# El resto de errores eran de identación y de espacios en blanco
# ya que al hacer un Format Document en el editor de código,
# se arreglan automáticamente.

# Faltaba un espacio antes y después del signo igual en el PI
PI = 3.14159

# Faltaban dos líneas en blanco entre la definición de la clase
# y la variable PI


class calculator:
    def __init__(self, name):
        # Faltaba un espacio antes y después del signo igual
        self.name = name

    # Faltaban espacios después de las comas

    def Add(self, a, b):
        # Estaba mal identado tenian que ser 2 espacios
        return a + b


# Faltaban dos líneas en blanco antes de la función


def compute_circle_area(radius):
    return PI * radius * radius


# Faltaban dos líneas en blanco antes de la función


def print_info(calc):
    # Faltaba un espacio después de la coma
    print("Calculator:", calc.name)


# Faltaban dos líneas en blanco antes de la variable


unused_variable = 42

# Faltaban dos líneas en blanco antes de la función


def divide(a, b):
    # Faltaba un espacio antes y después del signo igual
    if b == 0:
        return None
    return a / b


# Faltaban dos líneas en blanco antes de la función


def main():
    # Faltaba un espacio antes y después del signo igual
    c = calculator("Prova")
    print_info(c)
    # Faltaban espacios después de las comas
    print("Area", compute_circle_area(5))
    # Faltaban espacios después de las comas
    print("Sum:", c.Add(2, 3))
    # Faltaban espacios después de las comas
    print("Div:", divide(4, 0))


# Faltaban dos líneas en blanco antes del if
# Faltaba un espacio antes y después del doble igual
# EL main necesita estar en una línea aparte


if __name__ == "__main__":
    main()
