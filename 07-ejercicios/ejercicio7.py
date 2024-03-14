"""
Ejercicio 7.
    Hacer un programa que muestre todos los numeros impares
    entre 2 numeros que decida el usuarios.
"""

numero_1 = int(input("Introduce el primer numero: "))

numero_2 = int(input("Introduce el segundo numero: "))

if numero_1 < numero_2:
    for num in range(numero_1,numero_2):
        if not num % 2 == 0:
            print(f"Numero impar: {str(num)} ")
else:
    print("El numero 1 debe ser menor que el numero 2")