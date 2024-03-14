
# Excepciones personalizadas o lanzar excepcion

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("la edad introducidad no es real")
    elif len(nombre) <= 1 :
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al Master en Python {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Ha ocurrido un error: ",e)
