"""
Ejercicio de 2.
    Escribir un script que nos muestre en pantalla todos los numeros
    pares del 1 al 120
"""

num = 1

for num in range(1,121):
    if num % 2 == 0:
        print(num)