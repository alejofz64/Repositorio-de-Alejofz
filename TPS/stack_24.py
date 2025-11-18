from stack import Stack


mcu_stack = Stack()
aux_stack= Stack()

mcu_stack.push({"nombre": "Rocket Raccoon", "peliculas": 7})
mcu_stack.push({"nombre": "Groot", "peliculas": 6})
mcu_stack.push({"nombre": "Black Widow", "peliculas": 8})
mcu_stack.push({"nombre": "Iron Man", "peliculas": 10})
mcu_stack.push({"nombre": "Captain America", "peliculas": 9})
mcu_stack.push({"nombre": "Doctor Strange", "peliculas": 5})
mcu_stack.push({"nombre": "Gamora", "peliculas": 4})
mcu_stack.push({"nombre": "Drax", "peliculas": 4})
mcu_stack.push({"nombre": "Capitana Marvel", "peliculas": 3})

#A
posicion=0
while mcu_stack.size()>0:
    value = mcu_stack.pop()
    aux_stack.push(value)
    posicion+= 1
    if value['nombre']== 'Rocket Raccoon' or value['nombre']== 'Groot':
        print(value['nombre'], 'se encuentra en la posicion:', posicion)    

while aux_stack.size()>0:
    mcu_stack.push(aux_stack.pop())

#B
participacion5_stack = Stack()

while mcu_stack.size()>0:
    value = mcu_stack.pop()
    aux_stack.push(value)
    if value['peliculas']> 5:
        participacion5_stack.push(value)
while aux_stack.size()>0:
    mcu_stack.push(aux_stack.pop())
    
participacion5_stack.show()

#C
while mcu_stack.size()>0:
    value = mcu_stack.pop()
    aux_stack.push(value)
    if value['nombre'] == 'Black Widow':
        print('la viuda negra participo en: ', value['peliculas'])
while aux_stack.size()>0:
    mcu_stack.push(aux_stack.pop())

#D 
personajes_CDG = Stack()

while mcu_stack.size()>0:
    value = mcu_stack.pop()
    aux_stack.push(value)
    if value["nombre"][0].upper()== 'C' or  value["nombre"][0].upper()== 'D' or value["nombre"][0].upper()== 'G':
        personajes_CDG.push(value['nombre'])
        
while aux_stack.size()>0:
    mcu_stack.push(aux_stack.pop())
    
personajes_CDG.show()
print('aaaaaaaaaaaaaaaaa')
mcu_stack.show()