""""
Ejercicio 10.
    El programa tiene que pedir la nota de 15 alumnos
    y sacar por pantalla cuantos ha aprobado y cuantos han suspendido
"""

contador = 0
aprobados = 0
suspendidos = 0

numero_alumnos = int(input(f"¿Cuantos Alumnos tienes? : ")) 
while contador < numero_alumnos:
    contador += 1
    numero = int(input(f"Introduce la Nota del Alumno {str(contador)} : "))
    
    if numero >= 6 and numero <= 10:
        print(f"El Alumno {str(numero)} esta Aprobado")
        aprobados += 1
    else:
        print(f"El Alumno {str(numero)} esta NO Aprobado")
        suspendidos += 1
    


print(f"Total de alumnos calificados {str(contador)}")
print(f"Total de alumnos aprobados {str(aprobados)}")
print(f"Total de alumnos no aprobados {str(suspendidos)}")


