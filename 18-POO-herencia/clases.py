
class Persona:

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_apellidos(self):
        return self.apellidos

    def set_apellidos(self,apellidos):
        self.apellidos = apellidos

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando - bla bla bla"

    def caminar(self):
        return "Estoy caminando- tac tac tac"

    def dormir(self):
        return "Estoy durmiendo - Zzzzz"

class Informatico(Persona):

    def __init__(self):
        self.lenguajes = "HTML,CSS, Java, Python, JS, Node Js"
        self.experiencia = 5

    def get_lenguajes(self):
        return self.lenguajes

    def set_lenguajes(self,lenguajes):
        self.lenguajes = lenguajes

    def get_experiencia(self):
        return self.experiencia

    def set_experiencia(self,experiencia):
        self.experiencia = experiencia

    def programar(self):
        return "Estoy programando"

    def reparar_pc(self):
        return "Estoy reparando un PC"


class TecnicoRedes(Informatico):

    def __init__(self):
        self.auditar_redes = "Experto"
        self.experiencia_redes = 10

    def auditoria(self):
        return "Estoy auditando una red"