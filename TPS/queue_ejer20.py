from queue_ import Queue
from random import randint, choice

cabina_1 = Queue()
cabina_2 = Queue()
cabina_3 = Queue()

tipos_vehiculos = ["automovil", "camioneta", "camion", "colectivo"]

tarifas = {
    "automovil": 47,
    "camioneta": 59,
    "camion": 71,
    "colectivo": 64
}


#A
def agregar_vehiculos_aleatorios():
    for i in range(30):
       
        tipo_vehiculo = choice(tipos_vehiculos)
        cabina_seleccionada = randint(1, 3)
        
        if cabina_seleccionada == 1:
            cabina_1.arrive(tipo_vehiculo)
        elif cabina_seleccionada == 2:
            cabina_2.arrive(tipo_vehiculo)
        else:
            cabina_3.arrive(tipo_vehiculo)

#B C
def atencion_cabina_recaudacion (cabina_x):
    recaudado = 0 
    for i in range(cabina_x.size()):
        value = cabina_x.move_to_end()
        recaudado += tarifas[value]
    return recaudado

#D
def cantidad_por_vehiculo(cabina_x):
    vehiculos = {'automovil':0, 'camioneta':0, 'camion':0, 'colectivo':0}
    for i in range(cabina_x.size()):
        value = cabina_x.move_to_end()
        if value == 'automovil':
            vehiculos["automovil"]+=1
        elif value == 'camioneta':
            vehiculos["camioneta"]+=1
        elif value == 'camion':
            vehiculos["camion"]+=1
        else:
            vehiculos["colectivo"]+=1
    return vehiculos

#A       
agregar_vehiculos_aleatorios()

#B
recaudado_1= atencion_cabina_recaudacion(cabina_1)
recaudado_2= atencion_cabina_recaudacion(cabina_2)
recaudado_3= atencion_cabina_recaudacion(cabina_3)

# print(f'\n 1: {recaudado_1}, 2: {recaudado_2}, 3: {recaudado_3}')
# print()

if recaudado_2 < recaudado_1 > recaudado_3:
    print(f'\n La cabina que mas recaudo fue la cabina 1 con: {recaudado_1}$')
elif recaudado_2 > recaudado_3:
     print(f'\n La cabina que mas recaudo fue la cabina 2 con: {recaudado_2}$')
else:
     print(f'\n La cabina que mas recaudo fue la cabina 2 con: {recaudado_3}$')


print()
print(f'\n Vehiculos de la Cabina 1: {cantidad_por_vehiculo(cabina_1)}')
print(f'\n Vehiculos de la Cabina 2: {cantidad_por_vehiculo(cabina_2)}')
print(f'\n Vehiculos de la Cabina 3: {cantidad_por_vehiculo(cabina_3)}')
print()



# cabina_1.show()
# print()
# # cabina_2.show()
# # print()
# # cabina_3.show()
# print(atencion_cabina_recaudacion(cabina_1))
