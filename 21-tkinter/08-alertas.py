from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.geometry("800x800")
ventana.config(bd=50)

def sacarAlerta():
    MessageBox.showinfo("Info","Master en Python")
    #MessageBox.showwarning ("Info","Master en Python")
    #MessageBox.showerror ("Error","Ha ocurrido un error")

Button(ventana, text="Mostrar Alerta", command=sacarAlerta).pack()

def salir():
    resultado = MessageBox.askquestion("Info","Deseas Salir del Programa")
    if resultado != "yes":
        ventana.destroy()
    
   

Button(ventana, text="Salir", command=salir).pack()


ventana.mainloop()