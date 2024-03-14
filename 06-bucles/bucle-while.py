"""
# BUCLE WHILE
Estructura de control que itera o repite la ejecución de una
serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condición.

while condicion:
   bloque de instrucciones
   actualizacion de contador


"""


contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador} ")
    contador += 1

print("---------------------------------------")
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + " , " + str(contador)
    contador += 1

print(muestrame)


print("---------------------------------------")

numero = int(input("Numero a multiplicar?: "))

if(numero < 1):
    print("Introduce un numero mayor a 0")
else:
    contador = 1
    while contador <= 10:
         print(f"{numero} * {contador} = {numero * contador}")
         contador += 1
    else:
        print("Tabla finalizada.")
