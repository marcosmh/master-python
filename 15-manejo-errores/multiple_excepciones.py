
# Multiples excepciones

try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es " + str(numero*numero))
except TypeError:
    print("Debes converir tus cadenas a enteros en el codigo")
except ValueError:
    print("Introduce un numero valido")
except Exception as e:
    print("Ha ocurrido un error ", type(e).__name__)