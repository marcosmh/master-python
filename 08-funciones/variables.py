"""
Variables locales: se definen dentro de la funcion y no
se puede usar fuera de ella, solo estan disponibles dentro.

Variables globales: son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas

"""

# Variable global

frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres"

def holaMundo():
    frase = "Hola Mundo!!"
    print("Dentro de la funcion")
    print(frase)

    year = 2024
    print(year)

    global website
    website = "starwars.com"
    print("Dentro: ",website)

    return "Dato devuelto " + str(year)


holaMundo()
print(holaMundo())
print("Fuera", website)