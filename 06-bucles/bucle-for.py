"""
# BUCLE FOR

for variable in elemento_interable:  (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el "  + str(contador))

    resultado += contador

print(f"El resultado es: {resultado}")


print("\n########## Ejemplo 2 ############")

numero = int(input("Que numero deseas multiplicar?: "))
if numero < 1:
    print("Ingrese un numero mayor a 0")
else:
    for num_tabla in range(1,11):
        print(f"{numero} * {num_tabla} = {numero * num_tabla}")
    else:
        print("Tabla finalizada.")

