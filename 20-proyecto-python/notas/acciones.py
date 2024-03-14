import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"OK. {usuario[1]}!! Vamos a crear un nueva nota...\n")
        titulo = input("\nEscribe el Titulo de tu nota: ")
        descripcion = input("\nEscribe la Descripcion de tu nota: ")
        print("\n")

        if len(titulo) > 0:
            nota = modelo.Nota(usuario[0], titulo, descripcion)
            registro = nota.guardar()
            if registro[0] >= 1:
                print("La Nota se ha registrado correctamente.")
            else:
                print("No se pudo guardar la nota")
        else:
            print("Debe escribir un Titulo para guardar la nota.")

        
    def mostrar(self,usuario):
        print(f"\n=== Listado de Notas de {usuario[1]} === \n")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        print(len(notas))
        if len(notas) > 0:
            
            for n in notas:
                print("****** Listado de Notas *********")
                print(n[2])
                print(n[3])
                print("\n")
        else:
            print(f"No se encontraron notas para : {usuario[1]}")


    def borrar(self, usuario):
        print(f"\n Eliminar la nota {self.titulo} \n")

        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se ha Eliminado la nota. {nota.titulo} ")
        else:
            print(f"No se pudo Eliminar la nota. {nota.titulo}")

