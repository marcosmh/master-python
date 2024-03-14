"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer una funcion que recorra listas de numeros y devuelva un string
- Ordernarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento ( que el usuario pida por teclado )

"""
print(" Recorrer la lista y mostrarla ")
lista_numeros = [8,7,5,5,6,3,2,9]
for num in lista_numeros:
    print(f"Numero: {num}")

print("********************************************")
print(" Hacer una funcion que recorra listas de numeros y devuelva un string ")
def ver_lista(lista_num):
    resultado = ""
    for numx in lista_num:
        resultado += str(numx)
        resultado += "\n"

    return resultado

print(ver_lista(lista_numeros))
print(ver_lista(["Burzum","Mayhem","Emperor","Immortal"]))

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

print(" Ordernarla y mostrarla ")
lista_numeros.sort()
print(lista_numeros)
print("********************************************")

print(" Mostrar su longitud ")
print(len(lista_numeros))
print("********************************************")

print(" Buscar algun elemento ( que el usuario pida por teclado ) ")
buscar_num = int(input("Escribe el numero a buscar: "))
existe_num = buscar_num in lista_numeros
search_num = lista_numeros.index(buscar_num)

if existe_num:
    print(f"Si existe el numero {buscar_num} en la lista y esta en la posicion {search_num}. ")
else:
    print("Numero no encontrado en la lista")

