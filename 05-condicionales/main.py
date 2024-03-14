"""
 # Condicional IF

 SI se cumple_esta_condicion:
    Ejecutar grupo de instrucciones
 SI NO:
    Se ejecutan otro tipo de instrucciones

  if condicion:
     instrucciones
  else:
    otras instrucciones

# Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor igual que
>= mayor igual que    

# Operadores logico

and Y
or  O
!   negaacion
not no

"""

# Ejemplo 1
print("######### EJEMPLO 1 ###########")

#color = "rojo"
color = input("Adivina cual es mi color Favorito: ")
color="x"

if color  == "rojo":
   print("Mi color favorito es color ROJO")
else:
   print("El color es incorrecto")


print("######### EJEMPLO 2 ###########")

# year = 2020
year = input("En año actual: ")
year = 2024

if int(year) >= 2024:
   print("Estamos de 2024 en adelante !!")
else:
   print("ES una año anterior al actual")


print("######### EJEMPLO 3 ###########")

nombre = "Marcos Magaña"
ciudad = "Mexico"
continente = "America"
edad = 40
mayoria_edad = 18

if edad >= mayoria_edad:
   print(f"{nombre} es mayor de edad !!")

   if continente  != "America":
      print(f"{nombre} no es Americano")
   else:
      print(f"{nombre} es Americano y de la Ciudad de {ciudad}")
else:
   print(f"{nombre} No es mayor de edad !!")



print("######### EJEMPLO 4 ###########")

dia = int(input("Introduce el numero del dia de la semana: "))

if dia == 1:
   print("Es luner")
elif dia  == 2:
   print("Es martes")
elif dia == 3:
   print("Es miercoles")
elif dia == 4:
   print("Jueves")
elif dia == 5:
   print("Es viernes")
elif dia == 6:
   print("Es sabado")
elif dia == 7:
   print("Es domingo")
else:
   print("Los dias de la semana son 7")

print("######### EJEMPLO 5 ###########")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("¿Tienes edad de Trabajar ? Introduce tu Edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
   print("Esta en edad de trabajar")
else:
   print("No esta en edad de trabajar")



print("######### EJEMPLO 6 ###########")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
   print(f"{pais} es un pais de habla hispana !! ")
else:
   print(f"{pais} no es un pais de habla hispana :( ")


print("######### EJEMPLO 7 ###########")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
   print(f"{pais} NO es un pais de habla hispana !! ")
else:
   print(f"{pais} SI es un pais de habla hispana :( ")


print("######### EJEMPLO 8 ###########")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
   print(f"{pais} NO es un pais de habla hispana !! ")
else:
   print(f"{pais} SI es un pais de habla hispana :( ")