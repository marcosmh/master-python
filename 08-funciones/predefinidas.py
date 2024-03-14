nombre = "Marcos Magana"

#funciones generales
print(nombre)
print(type(nombre))

# detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa vaiable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero decimal")


# limpiar espacios

frase = "    mi contenido    "
print(frase.strip())

# eliminar variables
year = 2024
print(year)
#del year
#print(year)

# comprobar variale vacia
texto = " ff  "
if len(texto) > 0:
    print("Si tiene datos ", len(texto))
else:
    print("No contiene datos")


# encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

# reemplazar palabras en un string
nueva_frase = frase.replace("vida","xxx")
print(nueva_frase)

# mayusculas y minisculas
print(nombre)
print(nombre.lower())
print(nombre.upper())