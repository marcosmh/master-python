from coche import Coche

carro = Coche("Rojo","Ford","Mustang",350,550, 4)
carro2 = Coche("Amarillo","Ferrari","Murcielago",400,300, 2)
carro3 = Coche("Negro","VW","Jetta",300,200, 4)
carro4 = Coche("Gris","Nissan","Versa",300,200, 4)



print(carro.get_info())
print(carro2.get_info())
print(carro3.get_info())
print(carro4.get_info())
print(type(carro))

if type(carro) == Coche:
    print("Esta variable es de tipo Coche")
else:
    print("Es variable es de otro tipo.")

# Visibilidad

print(carro.soy_publico)
print(carro.get_soy_privado())