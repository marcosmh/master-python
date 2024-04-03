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
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=360,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)
    
    # Campos del formulario Añadir
    add_name_label.grid(row=1, column=0, padx=6, pady=6, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=6, pady=6, sticky=W)

    add_price_label.grid(row=2, column=0, padx=6, pady=6, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=6, pady=6, sticky=W)

    add_description_label.grid(row=3, column=0, padx=6, pady=6, sticky=E)
    add_description_entry.grid(row=3, column=1, padx=6, pady=6, sticky=W)
    #add_description_entry.config(width=30,font=("Consolas", 12),padx=16,pady=16)

    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=NW)
    boton.config(padx=16, pady=6, bg="green", fg="red")
    
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
    

# Variables
name_data = StringVar()
price_data = StringVar()    
description_data = StringVar()

# Definir pantalla Inicio
home_label = Label(ventana, text="Inicio")

# Definir pantalla Añadir
add_label = Label(ventana, text="Añadir")

# Campos del formulario
add_name_label = Label(ventana, text="Nombre: ")
add_name_entry = Entry(ventana,textvariable=name_data)

add_price_label = Label(ventana, text="Precio: ")
add_price_entry = Entry(ventana,textvariable=price_data)

add_description_label = Label(ventana, text="Descripción: ")
add_description_entry = Entry(ventana,textvariable=description_data)

add_separator = Label(ventana)

boton = Button(ventana, text="Guardar")



# Definir pantalla Información
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Marcos Magaña -  2024")

# cargar pantallas
#home()
add()
#info()

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