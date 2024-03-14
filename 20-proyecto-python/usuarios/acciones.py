import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("OK! Vamos a registrarte al sistema\n")
        nombre = input("Cual es tu nombre: ")
        apellidos = input("Cuales son tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        
        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print("El usuario se ha registrado correctamente.")
            print(f"{registro[1].nombre} - {registro[1].email} ")
        else:
            print("No se pudo registrar el usuario")



    def login(self):
        print("\nVale! identificate en el sistema\n")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        
        usuario = modelo.Usuario('','',email,password)
        login = usuario.identificar()

        try:

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema. {login[5]} ")
                self.proximasAcciones(login)
            else:
                print("Email o password Incorrecto. ")
        except Exception as e:
            print(type(e))
            print(type(e.__name__))
            print("Error al hacer el Login!")
        

    
    def proximasAcciones(self,usuario):
        print("""
                Acciones Disponibles:
                    - Crear nota (crear)
                    - Mostrar tus notas (mostrar)
                    - Eliminar nota (eliminar)
                    - Salir (salir)
              """)
        print("\n")
        
        accion = input("\nQue quieres hacer?: ")
        hazEl = notas.acciones.Acciones()


        if accion == "crear":
            print("\n === Crear Notas === \n")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("\n Mostrar Notas ===")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("\n === Eliminar Notas === \n")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Listo. {usuario[1]} hasta pronto. ")
            exit()
        else:
            print("Seleccione una opcion valida del menu.")
