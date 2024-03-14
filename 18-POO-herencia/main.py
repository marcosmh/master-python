import clases

persona = clases.Persona()
persona.set_nombre("Marcos")
persona.set_apellidos("Magana")
persona.set_altura("170cm")
persona.set_edad(30)

print(f"La persona es {persona.get_nombre()} {persona.get_apellidos()} - Altura: {persona.get_altura()} - Edad: {persona.get_edad()}")
print(persona.hablar())
print("\n")

informatico = clases.Informatico()
informatico.set_nombre("José")
informatico.set_apellidos("Robles")
informatico.set_altura("170cm")
informatico.set_edad(40)

print(f"Es informatico es {informatico.get_nombre()} {informatico.get_apellidos()} - Altura: {informatico.get_altura()} - Edad: {informatico.get_edad()}")
print(informatico.get_lenguajes())
print(informatico.programar())
print("\n")

tecnicoRedes = clases.TecnicoRedes()
tecnicoRedes.set_nombre("Mario")
tecnicoRedes.set_apellidos("Alvarez")
tecnicoRedes.set_altura("170cm")
tecnicoRedes.set_edad(35)

print(f"El tecnico es {tecnicoRedes.get_nombre()} {tecnicoRedes.get_apellidos()} - Altura: {tecnicoRedes.get_altura()} - Edad: {tecnicoRedes.get_edad()}")
print(tecnicoRedes.hablar())
print(tecnicoRedes.auditoria())