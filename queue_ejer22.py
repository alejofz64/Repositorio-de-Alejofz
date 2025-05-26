from queue_ import Queue

heroe_queue = Queue()

personajes = [
        {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
        {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
        {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
        {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
        {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
        {"nombre": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
        {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
        {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
        {"nombre": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
        {"nombre": "Shuri", "superheroe": "Black Panther", "genero": "F"},
        {"nombre": "Thor Odinson", "superheroe": "Thor", "genero": "M"},
        {"nombre": "Gamora", "superheroe": "Gamora", "genero": "F"},
        {"nombre": "Loki Laufeyson", "superheroe": "Loki", "genero": "M"},
        {"nombre": "Pepper Potts", "superheroe": "Rescue", "genero": "F"},
        {"nombre": "Bucky Barnes", "superheroe": "Winter Soldier", "genero": "M"},
    ]
#A
for personajes in personajes:
    heroe_queue.arrive(personajes)
    
for i in range(heroe_queue.size()):
    value = heroe_queue.move_to_end()
    if value['superheroe'] == 'Capitana Marvel':
        print(f'\n El nombre de la Capitana Marvel es: {value['nombre']}')
#B
print()
for i in range(heroe_queue.size()):
    value = heroe_queue.move_to_end()
    if value['genero'] == 'F':
        print(value['superheroe'])

#C
print()
for i in range(heroe_queue.size()):
    value = heroe_queue.move_to_end()
    if value['genero'] == 'M':
        print(value['superheroe'])

#D
print()
for i in range(heroe_queue.size()):
    value = heroe_queue.move_to_end()
    if value['nombre'] == 'Scott Lang':
        print(f'\n EL nombre del personaje de Scott Lang es: {value['superheroe']}')

#E
print()
for i in range(heroe_queue.size()):
    value = heroe_queue.move_to_end()
    if value['superheroe'][0] == 'S':
        print(value)

#F
#determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
encontrado = False

for i in range(heroe_queue.size()):
    value = heroe_queue.move_to_end()
    if value['nombre'] == 'Carol Danvers':
        encontrado = True
        print(f'\n El personaje Carol Danvers tiene como nombre de superheroe a: {value['superheroe']}')
        
if not encontrado:
    print('El personaje Carol Danvers no fue encontrado')

    
# heroe_queue.show()


