from tkinter import *

ventana = Tk()
ventana.title = "Formularios Avanzados"
ventana.geometry("800x800")


encabezado = Label(ventana, text="Formularios Avanzados")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas",20)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)


# Botones check
Label(ventana, text="A que te dedicas? ").grid(row=1, column=0)
Checkbutton(ventana, text="Desarrollo Web").grid(row=2, column=0)
Checkbutton(ventana, text="Desarrollo Movil").grid(row=3, column=0)



ventana.mainloop()