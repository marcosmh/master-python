"""
  Funciones:
  Una funcion es un conjunto de instrucciones agrupadas bajo un nombre
  concreto que pueden reutilizarse invocando a la funcion tantas veces
  como sea necesario
  
  def nombreDeMifuncion(parametros):
      # Bloque / Conjunto de instrucciones


  nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1
print("####### EJEMPLO 1 ########")

# Definir funcion
def muestraNombre():
      print("Marcos")
      print("Manuel")
      print("Juan")
      print("Nestor")
      print("\n")

muestraNombre()

# Ejemplo 2
print("####### EJEMPLO 2 ########")

def mostrartuNombre(nombre, edad):
      print(f"Tu nombre es {nombre}")

      if edad >= 18:
            print("Ya eres mayor de edad")
      else:
            print("Eres menor de edad")


nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrartuNombre(nombre, edad)

# Ejemplo 3
print("\n####### EJEMPLO 3 ########")

def tabla(numero):
      print(f"Tabla de multiplicar del numero: {str(numero)}")
      
      for contador in range(1,11):
            operacion = numero * contador
            print(f"{numero} x {contador} = {operacion}")
      
      print("\n")


numerox = int(input("Introduce el numero de la tabla: "))
tabla(numerox)

# Ejemplo 3.1
print("\n####### EJEMPLO 3.1 ########")
for numero_tabla in range(1,11):
      tabla(numero_tabla)
else:
      print("### FIN ###")


# Ejemplo 4
print("\n####### EJEMPLO 4 ########")
# Parametros opciones

def get_empleado(nombre, dni = None):
      print("EMPLEADO")
      print(f"Nombre: {nombre}")
      if dni != None:
         print(f"DNI: {dni}")


get_empleado("Marcos",123)
get_empleado("Marcos")



# Ejemplo 5
print("\n####### EJEMPLO 5 ########")

def saludame(nombre):
      saludo = f"Hola, Saludos {nombre}"

      return saludo

print(saludame("Marcos"))


# Ejemplo 6
print("\n####### EJEMPLO 6 ########")

def calculadora(numero_1, numero_2, basicas = False):
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


print(calculadora(10,4,True))
print(calculadora(10,4))
          

# Ejemplo 7
print("\n####### EJEMPLO 6 ########")

def get_nombre(nombre):
     texto = f"El nombre es: {nombre}"
     return texto


def get_apellidos(apellidos):
     texto = f"Los apellidos son: {apellidos}"
     return texto

def get_nombre_completo(nombre, apellidos):
     texto = get_nombre(nombre) + "\n" + get_apellidos(apellidos)
     return texto 


print(get_nombre("Marcos"))
print(get_apellidos("Magana H"))
print(get_nombre("Marcos"), get_apellidos("Magana H"))
print(get_nombre_completo("Marcos","Magana H"))

# Ejemplo 8: Funciones lambda
print("\n####### EJEMPLO 8 ########")

dime_el_anio = lambda anio: f"El año es {anio + 1}"

print(dime_el_anio(2024))