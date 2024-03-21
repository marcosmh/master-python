from tkinter import *

ventana = Tk()
ventana.title("Formularios en Tkinter | Master en Python")
ventana.geometry("800x800")

# Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#Label para el campo (nombre)
label = Label(ventana, text="Nombre: ")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Campo de texto (nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

#Label para el campo (apellidos)
label = Label(ventana, text="Apellidos: ")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Campo de texto (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

#Label para el campo (descripcion)
label = Label(ventana, text="Descripción: ")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Campo textarea (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, sticky=W, padx=5, pady=5)
campo_grande.config(width=30, height=5,font=("Arial",12), padx=15, pady=10)

# Boton
# Separador
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10, bg="green", fg="blue")

ventana.mainloop()