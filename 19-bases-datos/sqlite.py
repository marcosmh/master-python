import sqlite3

conexion = sqlite3.connect('pruebas.db')


# Crar cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "titulo varchar(255), " +
               "descripcion text, " +
                "precio int (255) " +
               " )")

"""
cursor.execute("INSERT INTO productos VALUES (null, 'Producto1','Desc Producto1',500) ")
conexion.commit()
"""

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
#print(productos)


cursor.execute("UPDATE productos SET titulo = 'Producto2', descripcion = 'Desc Producto2', precio = 300 WHERE id = 2 ")
cursor.execute("UPDATE productos SET titulo = 'Producto3', descripcion = 'Desc Producto3', precio = 200 WHERE id = 3 ")
cursor.execute("UPDATE productos SET titulo = 'Producto4', descripcion = 'Desc Producto4', precio = 700 WHERE id = 4 ")

#cursor.execute("DELETE FROM productos WHERE id = 5")
conexion.commit()

for producto in productos:
    print(producto)

conexion.close()