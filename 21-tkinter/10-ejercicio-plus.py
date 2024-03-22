"""
Calculadora:
- 2 campos de texto
- 4 botones para las operaciones
- Motrar el resultador en una alerta
"""
from tkinter import *
from tkinter import messagebox as Messagebox

class Calculadora():
   
    def __init__(self,Messagebox):
         self.numero1 = StringVar()
         self.numero2 = StringVar()
         self.resultado = StringVar()
         self.Messagebox = Messagebox



    def sumar(self):
        valida = self.validar(self.numero1, self.numero2)
        if valida == "continuar":
            try:
                self.resultado.set(float(self.numero1.get()) +  float(self.numero2.get()))
                self.mostrar_resultado("Suma",f"El resultado de la suma es: {self.resultado.get()}")
            except Exception as e:
                self.mostrar_error(e)
        else:
            self.Messagebox.showwarning("Warning",valida)

    def restar(self):
        valida = self.validar(self.numero1, self.numero2)
        if valida == "continuar":
            try: 
                self.resultado.set(float(self.numero1.get()) -  float(self.numero2.get()))
                self.mostrar_resultado("Resta",f"El resultado de la resta es: {self.resultado.get()}")
            except Exception as e:
                self.mostrar_error(e)
        else:
            self.Messagebox.showwarning("Warning",valida)

    def multiplicar(self):
        valida = self.validar(self.numero1, self.numero2)
        if valida == "continuar":
            try:
                self.resultado.set(float(self.numero1.get()) *  float(self.numero2.get()))
                self.mostrar_resultado("Multiplicar",f"El resultado de la multiplicación es: {self.resultado.get()}")
            except Exception as e:
                self.mostrar_error(e)
        else:
            self.Messagebox.showwarning("Warning",valida)

    def dividir(self):
        valida = self.validar(self.numero1, self.numero2)
        if valida == "continuar":
            try:
                self.resultado.set(float(self.numero1.get()) /  float(self.numero2.get()))
                self.mostrar_resultado("Dividir",f"El resultado de la división es: {self.resultado.get()}")
            except Exception as e:
                self.mostrar_error(e)
        else:
            self.Messagebox.showwarning("Warning",valida)

    def validar(self,numero1, numero2):
        result = "continuar"
        if len(numero1.get()) == 0:
            result = "El Primer número no debe ser nulo."
        elif len(numero2.get()) == 0:
            result = "El Segundo número no debe ser nulo."
        
        return result


    def mostrar_resultado(self,enc,msg):
        self.Messagebox.showinfo(enc,msg)
        self.numero1.set("")
        self.numero2.set("")

    def mostrar_error(self,e):
        error1 = e
        error2 = type(e).__name__
        self.Messagebox.showerror("Exception: ",f"Ha ocurrido un Error. {error1} -  {error2} ")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.title = "Ejercicicio completo con Tkinter"
ventana.geometry("400x400")
ventana.config(bd=26)

calculadora = Calculadora(Messagebox)

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
Entry(marco, textvariable=calculadora.numero1, justify=CENTER).pack(anchor=NW)

Label(marco, text="Segundo número: ").pack(anchor=NW)
Entry(marco, textvariable=calculadora.numero2, justify=CENTER).pack(anchor=NW)

Label(marco, text="").pack()


Button(marco,text="Sumar", command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco,text="Restar", command=calculadora.restar).pack(side=LEFT,fill=X, expand=YES)
Button(marco,text="Multiplicar", command=calculadora.multiplicar).pack(side=LEFT,fill=X, expand=YES)
Button(marco,text="Dividir", command=calculadora.dividir).pack(side=LEFT,fill=X, expand=YES)


ventana.mainloop()