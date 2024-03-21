from tkinter import *

ventana = Tk()
ventana.geometry("800x600")

texto = Label(ventana, text="Bienvenido a mi Programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas",30)
)
texto.pack()

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, tu eres de {pais}"

texto = Label(ventana, text=pruebas("Marcos","Magaña","México"))
texto.config(
    font=("Consolas",15),
    #justify=RIGHT
    width=400,
    height=400,
    cursor="circle"

)
texto.pack(anchor=SE)



ventana.mainloop()