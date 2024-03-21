from tkinter import *

ventana = Tk()
#ventana.geometry("800x600")

texto = Label(ventana, text="Bienvenido a mi Programa")
texto.config(
    fg="white",
    bg="black",
    padx=10,
    pady=20,
    font=("Consolas",30)
)
texto.pack(side=TOP, fill=X)

texto = Label(ventana, text="Dev Python")
texto.config(
    #height=3,
    bg="green",
    padx=10,
    pady=20,
    font=("Consolas",30),
    cursor="spider"
)
texto.pack(side=TOP,fill=X, expand=YES)

texto = Label(ventana, text="Code Python-1")
texto.config(
    height=3,
    bg="red",
    padx=10,
    pady=20,
    font=("Consolas",30),
    cursor="spider"
)
texto.pack(side=LEFT,fill=X, expand=YES)

texto = Label(ventana, text="Code Python-2")
texto.config(
    height=3,
    bg="blue",
    padx=10,
    pady=20,
    font=("Consolas",30),
    cursor="spider"
)
texto.pack(side=LEFT,fill=X, expand=YES)

texto = Label(ventana, text="Code Python-3")
texto.config(
    height=3,
    bg="brown",
    padx=10,
    pady=20,
    font=("Consolas",30),
    cursor="spider"
)
texto.pack(side=LEFT,fill=X, expand=YES)




ventana.mainloop()