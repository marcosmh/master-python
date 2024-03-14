"""
Ejercicio 5. 
    Hacer un programa que muestre todos los numeros
    entre dos numeros que diga que el usuario
"""

numero_1 = int(input("Introduce el primer numero: "))

numero_2 = int(input("Introduce el segundo numero: "))

contador = 1

if numero_1 < numero_2:        
    for contador in range(numero_1, numero_2):
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")
    