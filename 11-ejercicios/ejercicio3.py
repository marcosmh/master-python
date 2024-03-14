"""
Ejercicio 3.
Programa que compruebe si una variable esta vacia
y si esta vacia, rellenarla con texto en minusculas y
mostrarlo en minisulas

"""

texto = ""

if len(texto) == 0:
    texto = "Conoces la tragedia de Dark Plaguies"
    print(texto.lower())
    print(texto.upper())
else:
    texto = "Look yo soy tu padre"
    print(texto.lower())
    print(texto.upper())
