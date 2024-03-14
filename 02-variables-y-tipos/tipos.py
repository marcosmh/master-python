# variables
nada = None
cadena = "Master en Python"
numero = 5
decimal = 5.5
booleano = True
lista = [10,20,30,40,50]
listaString = [20,"treinta",40,"cincuenta"]
tuplaNoCambia = ("Master","En","Python")
dicccionario = {
    "nombre": "Marcos",
    "apellido": "Magaña",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"

# imprimir variable
print(nada)
print(cadena)
print(numero)
print(decimal)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(dicccionario)
print(rango)
print(dato_byte)

# mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(numero))
print(type(decimal))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(dicccionario))
print(type(rango))
print(type(dato_byte))


print("Convertir un tipo de dato a otro")

texto = "El numero es "
numerito = 88
numerox = "77"
numeroy = "8.8"

print(texto +" "+str(numerito))

print(11+int(numerox))
print(1.1+float(numeroy))