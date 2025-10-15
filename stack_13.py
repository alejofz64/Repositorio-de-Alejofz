from stack import Stack


trajes_stack = Stack()

#D E
while True:
    modelo = input('Ingresa el modelo (o "s" para salir): ')
    if modelo.lower() == 's':
        break
        
    pelicula = input('Ingresa la película: ')
    estado = input('Ingresa el estado: ')
    new_traje = {'modelo': modelo, 'pelicula': pelicula, 'estado': estado}

    # Verificar duplicados
    duplicado = False
    temp_stack = Stack()
    
    while trajes_stack.size() > 0:
        traje = trajes_stack.pop()
        temp_stack.push(traje)
        if (traje['modelo'] == new_traje['modelo'] and 
            traje['pelicula'] == new_traje['pelicula']):
            duplicado = True
            print('Este traje ya está registrado')
            
    # Restaurar pila original
    while temp_stack.size() > 0:
        trajes_stack.push(temp_stack.pop())
        
    if not duplicado:
        trajes_stack.push(new_traje)
    

trajes_stack.push({"modelo": "Mark I", "pelicula": "Iron Man", "estado": "Dañado"})
trajes_stack.push({"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"})
trajes_stack.push({"modelo": "Mark III", "pelicula": "Iron Man 2", "estado": "Impecable"})
trajes_stack.push({"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"})  
trajes_stack.push({"modelo": "Mark XLIV", "pelicula": "Avengers: Infinity War", "estado": "Destruido"})


# A
encontrado=False
pelicula_traje= Stack()
aux_stack = Stack()

while trajes_stack.size() > 0:
    traje= trajes_stack.pop()
    aux_stack.push(traje)
    if traje['modelo'] == 'Mark XLIV':
        encontrado=True
        pelicula_traje.push(traje['pelicula'])
        
while aux_stack.size() > 0:
        trajes_stack.push(aux_stack.pop())
        
if encontrado:
    print('El traje fue utilizado en: ')
    while pelicula_traje.size() > 0:
        value = pelicula_traje.pop()
        print(value)
        
else:
    print('El traje no fue utilizado')
    
# B
aux_stack = Stack()
trajes_dañados= Stack()

while trajes_stack.size()>0:
    traje= trajes_stack.pop()
    aux_stack.push(traje)
    if traje['estado'] == 'Dañado':
        trajes_dañados.push(traje['modelo'])
        
while aux_stack.size()>0:
    trajes_stack.push(aux_stack.pop())
    
print('Los modelos que resultaron dañados son: ')
while trajes_dañados.size()>0:
    value=trajes_dañados.pop()
    print(value)

# C

while trajes_stack.size()>0:
    traje= trajes_stack.pop()
    if traje['estado']== 'Dañado':
        print(traje['modelo'],'fue elimindo')
    else:
        aux_stack.push(traje)

while aux_stack.size()>0:
    trajes_stack.push(aux_stack.pop())
    

#F
print('Modelos utilizados en Spider-Man: Homecoming y Capitan America: Civil War ')
while trajes_stack.size() > 0:
    value = trajes_stack.pop()
    aux_stack.push(value)
    if value['pelicula'] == 'Spider-Man: Homecoming' or value['pelicula'] == 'Capitan America: Civil War':
        print(value['modelo'])
        
while aux_stack.size()>0:
    trajes_stack.push(aux_stack.pop())
    
trajes_stack.show()