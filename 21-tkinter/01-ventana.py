
from tkinter import *
import os.path

class Programa:
   
   def __init__(self):
        self.title = "Interfaz Gráfica con Python y Tkinter"
        self.icon = "./imagenes/python.ico"
        self.icon_alt = "./21-tkinter/imagenes/python.ico"
        self.size = "800x600"
        self.resizable = False

    
   def cargar(self):
        
        # Crear ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #Titulo de la ventana
        ventana.title(self.title)

        # comprobar si exite el archivo
        ruta_icono = os.path.abspath(self.icon)
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        if os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)
            
        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)


        # Cambio de el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

        # Arrancar y mostrar la ventana hasta que se cierre
        # ventana.mainloop()

   def add_texto(self,dato):
       texto = Label(self.ventana, text = dato)
       texto.pack()

   def mostrar(self):
       self.ventana.mainloop()


# Instanciar Programa
programa = Programa()
programa.cargar()
programa.add_texto("Hola Mundo desde Tkinter")
programa.add_texto("Python es la Ley")
programa.mostrar()