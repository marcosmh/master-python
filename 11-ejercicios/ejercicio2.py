"""
Ejercicio 2.
- Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y mostrar las lista.

- usar while y for

"""

lista_numeros = []

cont = 0
while(cont < 120):
    lista_numeros.append(f"elemento-{cont}")
    print("Mostrando el: " + lista_numeros[cont])
    cont += 1
else:
    print(lista_numeros)
    print("Lista terminada")

print(lista_numeros[77])

print("******************************************")

for contador in range(0,120):
    lista_numeros.append(f"elemento-{contador}")
    #print("Mostrando el: " + lista_numeros[contador])
else:
    print(lista_numeros)
    print("Lista terminada")

#print(lista_numeros[119])


