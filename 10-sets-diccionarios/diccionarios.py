"""
Diccionario:
 Un tipo de dato que almacena un conjunto de datos.
 En formator clave -> valor
 Es parecid a un arrat asociativo o un objeto Json

"""

persona = {
    "nombre": "Marcos",
    "Apellidos": "Magana",
    "web": "001"
}

print(type(persona))
print(persona)
print(persona["nombre"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Marcos',
        'email': 'marcos@x.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@x.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'chava@x.com'
    }
]

print(type(contactos))
contactos[1]['nombre'] = "Alfredo"
print(contactos)
print(contactos[0]['nombre'])

print("\n Listado de contactos")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-----------------------")