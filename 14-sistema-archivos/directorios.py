import os
import pathlib
import shutil

# Crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("Carpeta Creada.")
else:
    print("El directorio ya existe")


# Copiar carpeta
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"
shutil.copytree(ruta_original,ruta_nueva)
"""

#Eliminar carpeta
"""
os.rmdir("./mi_carpeta_COPIADA")
"""
print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
print(contenido)
for fichero in contenido:
    print("Fichero: " + fichero)


