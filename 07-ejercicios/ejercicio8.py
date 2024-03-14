"""
Ejercicio 8.
    ¿Cuanto es el X por ciento de X numero?

"""

numero_1 = int(input("Introduce un numero: "))

numero_2 = int(input("Cual porcentaje deseas aplicar: "))


porcentaje = numero_1 * (numero_2 / 100)
aumento = numero_1 + porcentaje

print(f"El {(numero_2)}% de {(numero_1)} es {str(porcentaje)} - el aumento es: {str(aumento)} ")