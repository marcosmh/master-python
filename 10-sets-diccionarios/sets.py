"""
SET es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden
"""

personas = {
    'Marcos',
    'Manuel',
    "Franciso"
}

personas.add("Carlos")
personas.remove("Manuel")
personas

print(type(personas))
print(personas)