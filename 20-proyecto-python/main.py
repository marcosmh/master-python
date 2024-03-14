"""
Proyecto Python y MySQL
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos un login, identifica al usuario y nos preguntará
- Crear notas, mostrar notas, borrarlas
"""
from usuarios import acciones

print("""
    Acciones Disponibles:
     - registro
     - login
""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
else:
    print("Accion Desconocida..")


