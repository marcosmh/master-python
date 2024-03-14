import datetime
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self,usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES(null,%s,%s,%s,NOW() )"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        try:
            cursor.execute(sql,nota)
            database.commit()
            print("Nota registrada correctamente en la bd.")
        except Exception as e:
            database.rollback()
            print("Exception: Error al registrar la nota. - ",e)

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE id = {self.usuario_id}"
        result = None
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print("Consulta ejecutada correctamente.")
        except Exception as e:
            print("Exception: Error al realizar la consulta. ", e )

        return result
        

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' "
        print(sql)
        result = None
        try:
            result = cursor.execute(sql)
            print(result)
            database.commit()
            print("La Nota se ha eliminado correctamente.")
        except Exception as e:
            print("Exception: Error al realizar la consulta. ", e )
        
        return [cursor.rowcount, self]