"""
Calculadora:
- 2 campos de texto
- 4 botones para las operaciones
- Motrar el resultador en una alerta
"""
from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.title = "Ejercicicio completo con Tkinter"
ventana.geometry("400x400")
ventana.config(bd=26)

def sumar():
    valida = validar(numero1, numero2)
    if valida == "continuar":
        try:
            resultado.set(float(numero1.get()) +  float(numero2.get()))
            mostrar_resultado("Suma",f"El resultado de la suma es: {resultado.get()}")
        except Exception as e:
            mostrar_error(e)
    else:
        Messagebox.showwarning("Warning",valida)

def restar():
    valida = validar(numero1, numero2)
    if valida == "continuar":
        try: 
            resultado.set(float(numero1.get()) -  float(numero2.get()))
            mostrar_resultado("Resta",f"El resultado de la resta es: {resultado.get()}")
        except Exception as e:
            mostrar_error(e)
    else:
        Messagebox.showwarning("Warning",valida)

def multiplicar():
    valida = validar(numero1, numero2)
    if valida == "continuar":
        try:
            resultado.set(float(numero1.get()) *  float(numero2.get()))
            mostrar_resultado("Multiplicar",f"El resultado de la multiplicación es: {resultado.get()}")
        except Exception as e:
            mostrar_error(e)
    else:
        Messagebox.showwarning("Warning",valida)

def dividir():
    valida = validar(numero1, numero2)
    if valida == "continuar":
        try:
            resultado.set(float(numero1.get()) /  float(numero2.get()))
            mostrar_resultado("Dividir",f"El resultado de la división es: {resultado.get()}")
        except Exception as e:
            mostrar_error(e)
    else:
        Messagebox.showwarning("Warning",valida)

def validar(numero1, numero2):
    result = "continuar"
    if len(numero1.get()) == 0:
        result = "El valor de numero1 no debe ser nulo."
    elif len(numero2.get()) == 0:
        result = "El valor de numero2 no debe ser nulo."
    
    return result


def mostrar_resultado(enc,msg):
    Messagebox.showinfo(enc,msg)
    numero1.set("")
    numero2.set("")

def mostrar_error(e):
    error1 = e
    error2 = type(e).__name__
    Messagebox.showerror("Exception: ",f"Ha ocurrido un Error. {error1} -  {error2} ")
    numero1.set("")
    numero2.set("")


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=360, height=360)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack(anchor=NW)
Entry(marco, textvariable=numero1, justify=CENTER).pack(anchor=NW)

Label(marco, text="Segundo número: ").pack(anchor=NW)
Entry(marco, textvariable=numero2, justify=CENTER).pack(anchor=NW)

Label(marco, text="").pack()


Button(marco,text="Sumar", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco,text="Restar", command=restar).pack(side=LEFT,fill=X, expand=YES)
Button(marco,text="Multiplicar", command=multiplicar).pack(side=LEFT,fill=X, expand=YES)
Button(marco,text="Dividir", command=dividir).pack(side=LEFT,fill=X, expand=YES)


ventana.mainloop()