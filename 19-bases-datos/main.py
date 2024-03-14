import mysql.connector

# conexion

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admindba"
)

if database.connection_id:
    print("Conexion OK")
else:
    print("Fallo al conectar a la base de datos")


# CREAR CURSOR
cursor = database.cursor()

#CREAR BASE DE DATOS
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute(""" USE master_python """)

# Crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS master_python.vehiculos(
    id     int(10) auto_increment not null,
    marca  varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")


# cursor.execute("INSERT INTO master_python.vehiculos VALUES(null,'Ford','Mustang',7500 ) ")

carros = [
    ('Seat','Ibiza',5000),
    ('Renault','Clio',6000),
    ('Citroen','Saxo',2000),
    ('Mercedes','Clase C',35000),
]

#cursor.executemany("INSERT INTO master_python.vehiculos VALUES(null,%s,%s,%s ) ",carros)

"""
cursor.execute("UPDATE master_python.vehiculos SET marca = 'Ferrari', modelo = 'Ferrari', precio = 8100.10 WHERE id = 2 ")

cursor.execute("DELETE FROM master_python.vehiculos WHERE id = 3 ")
"""

print(cursor.rowcount, "Datos")
database.commit()



print("Lista de Vehiculos")
cursor.execute("SELECT * FROM vehiculos")
vehiculos = cursor.fetchall()
for vehiculo in vehiculos:
    print(vehiculo)


database.close()