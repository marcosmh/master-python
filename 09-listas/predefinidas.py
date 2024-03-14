cantantes = ["2pac","Bon Jovi","Luis Miguel","Chico Che","Los Joao"]
numeros = [1,2,5,8,3,4]

# ordenar

print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
print(cantantes)
cantantes.append("Jose Jose")
print(cantantes)
cantantes.insert(0,"Julio Iglesias")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove("Los Joao")
print(cantantes)

# Revertir la lista

numeros.reverse()
print(numeros)

# Buscar en una lista
print("Chico Che" in cantantes)

# Contar numeros de elementos de la lista
print(len(cantantes))

# Cuantas veces aparece un elemento
print(numeros.count(8))

# conseguir un indice
print(cantantes.index("Chico Che"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)