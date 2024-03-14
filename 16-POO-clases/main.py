"""
Programacion orientada a objetos
"""
#Definir una clase
class Coche:
    # Atributos o propiedades
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos, son acciones que hace el objeto

    def set_marca(self,marca):
        self.marca = marca

    def get_marca(self):
        return self.marca
    def set_color(self,color):
        self.color = color

    def get_color(self):
        return self.color

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_velocidad(self):
        return self.velocidad

# fin de definicion de clase


#Crear objetos
print("---- Coche1 ---- ")
coche = Coche()
coche.set_color("Amarillo")

print(coche.marca, coche.get_modelo(), coche.get_color())
print("Velocidad actual: ",coche.get_velocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad actual: ",coche.get_velocidad())

print("\n--- Coche2 --- ")
coche_ford = Coche()
coche_ford.set_marca("Ford")
coche_ford.set_modelo("Mustang")
coche_ford.set_color("Azul")

print("Marca: " + coche_ford.get_marca() + " - " +
        "Modelo: " + coche_ford.get_modelo() +
        "Color: " + coche_ford.get_color() + " - " +
        "Velocidad: " + str(coche_ford.get_velocidad()))