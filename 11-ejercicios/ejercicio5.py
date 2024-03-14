"""
Ejercicio 5:
Crear una lista con el contenido de esta tabla:

ACCION  AVENTURA            DEPORTES
GTA     ASSINGS             FIFA 21
COD     CRASH               PRO 21
PUGB    PRINCE OF PERSIA    MOTO GP 21

"""

tabla = [

    {
        "categoria": "ACCION",
        "juegos": ["GTA","Call of Duty","PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["Assins Creed","CRASH","Prince of Persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21","PRO 21","Moto GP 21"]
    }

]

for categoria in tabla:
    print(f"---------- {categoria['categoria']} -----------")
    for juego in categoria['juegos']:
        print(juego)

