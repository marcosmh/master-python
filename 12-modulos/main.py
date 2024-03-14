"""
Modulos: son funcionalidades ya hechas para reutilizar

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet y tambien podemos crear nuestros modulos.

"""

"""
import mimodulo

print(mimodulo.holaMundo("Marcos"))
print(mimodulo.calculadora(10,3,True))
"""
"""
from mimodulo import holaMundo

print(holaMundo("Marcos"))
"""

from mimodulo import *

print(holaMundo("Marcos"))


# Modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

