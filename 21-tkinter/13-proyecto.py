"""
Crear un programa que tenga:
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, Añadir, Información, Salir)
- Opcion Salir
- Diferentes pantallas
- Formulario para añor productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
"""

from tkinter import *

# Definir ventana
ventana = Tk()
ventana.geometry("800x800")
ventana.title("Proyecto Tkinter - Master en Python")
#ventana.resizable(0,0)

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

# Pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=320,
        pady=20
    )
    home_label.grid(row=0, column=0)

    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()



def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=320,
        pady=20
    )
    add_label.grid(row=0, column=0)
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=320,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    home_label.grid_remove()
    add_label.grid_remove()
    
    

# Definir pantallas
home_label = Label(ventana, text="Inicio")
add_label = Label(ventana, text="Añadir")
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Marcos Magaña -  2024")

# cargar pantallas
home()
add()
info()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menú
ventana.config(menu=menu_superior)


# Cargar menu
ventana.mainloop()