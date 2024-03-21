from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("800x600")

texto = Label(ventana, text="Bienvenido a mi Programa")
texto.config(
    font=("Consolas",30)
)
texto.pack(anchor=W)

imagen = Image.open("./21-tkinter/imagenes/arcann.png")
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()


ventana.mainloop()