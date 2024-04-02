from tkinter import *

ventana = Tk()
ventana.geometry("800x800")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)

editar = Menu(mi_menu)
editar.add_command(label="Deshacer")
editar.add_command(label="Rehacer")
editar.add_separator()
editar.add_command(label="Copiar")
editar.add_command(label="Cortar")
editar.add_command(label="Pegar")

seleccionar = Menu(mi_menu, tearoff=0)
seleccionar.add_command(label="Seleccionar todo")
seleccionar.add_command(label="Expandir selección")
seleccionar.add_command(label="Reducir selección")
seleccionar.add_separator()
seleccionar.add_command(label="Copiar linea arriba")
seleccionar.add_command(label="Copiar linea abajo")


mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_cascade(label="Editar", menu=editar)
mi_menu.add_cascade(label="Selecionar", menu=seleccionar)


ventana.mainloop()