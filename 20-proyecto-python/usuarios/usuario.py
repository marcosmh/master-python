import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def cifrar_pwd(self,password):
        cifrado = hashlib.sha256()
        cifrado.update(password.encode('utf-8'))
        return cifrado.hexdigest()

    def registrar(self):
        fecha = datetime.datetime.now()

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))

        sql =  "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s) "
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql,usuario)
            database.commit()
            print("Usuario registrado correctamente en la bd.")        
        except Exception as e:
            database.rollback()
            print("Exception: Error al registrar al usuario. - ",e)

        return [cursor.rowcount, self]

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s "
        cifrado = self.cifrar_pwd(self.password)
        usuario = (self.email,cifrado)
        result = None
        
        try:
            cursor.execute(sql,usuario)
            result = cursor.fetchone()
            print("Se ha realizado la consulta correctamente. ")
        except Exception as e:
            print("Exception: Error al realizar la consulta. ", e )

        return result


    def to_string(self):
        result = ""
        result += "nombre: " + self.nombre + " "
        result += "apellidos: " + self.apellidos + " "
        result += "email: " + self.email
        return result