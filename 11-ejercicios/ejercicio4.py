"""
Ejercicio 4.
Crear un programa que tenga 4 variables, una lista, un string,
un entero y un bolleano y que imprima un mensaje segun el tipo
de dato de cada variable. Usar funciones
"""

lista = ["Heavy Metal","Death Metal","Black Metal"]
cadena = "Conoces la tragedia de Dark Plaguies?"
numero = 10
booleano = True

def traducir_tipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "String"
    elif tipo == int:
        result = "Entero"
    elif tipo == bool:
        result = "Booleano"
    else:
        result = "Desconocido"

    return result
def tipo_datos(dato,tipo):
    tipo_d = isinstance(dato,tipo)
    valor = traducir_tipo(tipo)
    mensaje = ""
    if tipo_d:
        mensaje = f"Esta Dato es del tipo: {valor} - {type(dato)}"
    else:
        mensaje = "Tipo de dato desconocido."

    return mensaje


print(tipo_datos(cadena,str))
print(tipo_datos(lista,list))
print(tipo_datos(numero,int))
print(tipo_datos(booleano,bool))

