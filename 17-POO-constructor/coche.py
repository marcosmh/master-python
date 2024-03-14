class Coche:
    # Atributos o propiedades
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Soy un atributo publico"
    __soy_privado = "Soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas,):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


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

    def set_caballaje(self,caballaje):
        self.caballaje = caballaje

    def get_caballaje(self):
        return self.caballaje

    def set_plazas(self,plazas):
        self.plazas = plazas

    def get_plazas(self):
        return self.plazas

    def get_soy_publico(self):
        return self.soy_publico

    def get_soy_privado(self):
        return self.__soy_privado

    def get_info(self):
        info = ""
        info += "Marca: " + self.get_marca() + " - "
        info += "Modelo: " + self.get_modelo() + " - "
        info += "Color: " + self.get_color() + " - "
        info += "Velocidad: " + str(self.get_velocidad()) + " - "
        info += "Caballaje: " + str(self.get_caballaje()) + " - "
        info += "Plazas: " + str(self.get_plazas())

        return info
# fin de definicion de clase