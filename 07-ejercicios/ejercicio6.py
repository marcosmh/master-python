"""
Ejercicio 6.
    Mostrar todas las tabla de multiplicar del 1 al 10.
    Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

print("Tablas de Multiplicar")

numero = 1
total_tablas = 10

for numero in range(1,11):
    print(f"\nTabla del Numero {str(numero)}")
    if numero <= 10:
        for num_tabla in range(1,11):                
            print(f"{numero} * {num_tabla} = {numero * num_tabla}")
        else:
            print("-----------------------\n")
    



