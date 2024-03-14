from io import open
import pathlib
import shutil
import os
import os.path


# abrir archivo
#archivo = open('fichero_texto.txt','a+')
"""
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta,"r")
"""
# Escribir archivo
# archivo.write("**** Hola Mundo ****\n")

# Cerrar archivo
#archivo.close()

# leer contenido
#contenido = archivo.read()
#print(contenido)

# Leer contenido y guardar en lista
"""
lista = archivo.readlines()
archivo.close()
print(lista)
for linea in lista:
    print(linea)
"""

# copiar archivos
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str("./alternativa/fichero_77.txt")
ruta_alternativa2 = str(pathlib.Path().absolute()) + "/alternativa/fichero_88.txt"
print(ruta_alternativa2)
shutil.copyfile(ruta_original,ruta_alternativa2)
"""

# Mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)
"""

# Eliminar
"""
ruta_nuevax = str(pathlib.Path().absolute()) + "/fichero_texto_NUEVO.txt"
print(ruta_nuevax)
os.remove(ruta_nuevax)
"""

# comprobar si existe un directorio

print(os.path.abspath(("./")))

ruta_comprobar = os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt")
print(ruta_comprobar)
if(ruta_comprobar):
    print("El archivo si existe")
else:
    print("El archivo no existe")