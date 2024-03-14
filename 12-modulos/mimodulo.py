def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"


def calculadora(numero_1, numero_2, basicas=False):
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multi = numero_1 * numero_2
    divi = numero_1 / numero_2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(divi)
        cadena += "\n"

    return cadena
