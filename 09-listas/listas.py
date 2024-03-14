"""
Listas (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""

pelicula = "Batman"
peliculas = ["Batman","Spiderman","El Señor de los Anillos"]
cantantes = list(("2pac","Bon Jovi","Luis Miguel"))
years = list(range(2020,2030))
variada = ["Marcos",30,4.4,True,"OK"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
# Indices
peliculas[1] = "X Men"

print(peliculas[1])
print(cantantes[-2])
print(years[0:2])
print(variada[3])
print(peliculas[1:])

# Añadir elementos a la lista

peliculas.append("The Hobbit")
cantantes.append("Chico Che")
print(peliculas)
print(cantantes)

# Recorrer la lista
print("-----------------------")

print("### Peliculas ####")
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Escribe una nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("### Listado de Peliculas ####")
for p in peliculas:
    print(f" {peliculas.index(p)+1}.  {p}")


# lista multidimencionales

print("\n **** Lista de Contactos ******")
contactos = [
    [
        'Marcos',
        'marcosœmarcode.com'
    ],
[
        'Jorge',
        'jorgeœmsn.com'
    ],
    [
        'Mario',
        'marioœyahoo.com'
    ],

]

for contacto in contactos:
    for elemento in contacto:
        print(elemento)

#print(contactos)
#print(contactos[1][1])
