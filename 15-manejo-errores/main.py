"""
Capturar excepciones y manejar errores de codigo
susceptible a fallos/errores

"""
try:
    nombre = input("¿Cual es tu nombre?: ")
    print(len(nombre))

    if len(nombre) > 0 :
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, Debe introducir un nombre.")
else:
    print("Ok")
finally:
    print("Fin del programa")

print("------------------------------------------")

numeros = [8,7,5,5,6,3,2,9]

try:
    busqueda = int(input("Introduce un numero: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce un numero: "))
    else:
        print(f"Has Introducido el {busqueda}")

    print(f"##### Buscar en la lista el numero {busqueda} #####")


    search = numeros.index(busqueda)
    print(f"El numero buscado existe en la lista, es el indice: {search}")
except:
    print("Ha ocurrido error. El numero no existe en la lista.")

