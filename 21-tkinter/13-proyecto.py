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
from tkinter import ttk

# Definir ventana
ventana = Tk()
#ventana.geometry("800x800")
ventana.minsize(800,800)
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
        padx=360,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)

    # Listar productos

    """
    for product in products:
        if len(products) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="-------------------").grid()
    """

    for product in products:
        if len(products) == 3:
            product.append("added")
            products_box.insert('',0, text=product[0], values=(product[1]))

    add_label.grid_remove()
    add_frame.grid_remove()
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
    add_frame.grid(row=1)
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
    products_box.grid_remove()
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

    add_frame.grid_remove()
    products_box.grid_remove()
    home_label.grid_remove()
    add_label.grid_remove()
    
def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        description_data.get()
        #add_description_entry.get("1.0","end-1c")
    ])
    name_data.set("")
    price_data.set("")
    description_data.set("")

    print(products)
    home()


# Variables
products = []
name_data = StringVar()
price_data = StringVar()    
description_data = StringVar()

# Definir pantalla Inicio
home_label = Label(ventana, text="Inicio")
#products_box = Frame(ventana, width=800)

Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

# Definir pantalla Añadir
add_label = Label(ventana, text="Añadir")

# Campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame,textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame,textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción: ")
#add_description_entry = Entry(add_frame)
add_description_entry = Entry(add_frame,textvariable=description_data)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)



# Definir pantalla Información
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