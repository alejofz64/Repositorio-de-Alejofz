
from superheroes_data import superheroes
from list_ import List
            
def order_by_name(item):
    return item.name

def order_by_real_name(item):
    return item.real_name

def order_by_first_appearance(item):
    return item.first_appearance


class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias 
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
        
    def __str__(self):
        return f'{self.name}, {self.real_name} - {self.is_villain} ({self.first_appearance})'

list_superhero = List()

list_superhero.add_criterion('name', order_by_name)


for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero)
    


#A Listado ordenado de manera ascendente por nombre de los personajes.
list_superhero.sort_by_criterion('name')
# list_superhero.show()

#B Determinar en que posicion esta The Thing y Rocket Raccoon.
print()

posicion = list_superhero.search('The Thing','name')
print(f' The Thing se encuentra en la posicion {posicion}')

posicion = list_superhero.search('Rocket Raccoon','name')
print(f' Rocket Raccoon se encuentra en la posicion {posicion}')

#C Listar todos los villanos de la lista.
print()

for superhero in list_superhero:
    if superhero.is_villain == True:
        # print(superhero)
        pass

#D Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980
from queue_ import Queue
cola_superheroes = Queue()

for superhero in list_superhero:
    if superhero.is_villain == True:
        cola_superheroes.arrive(superhero)

for i in range(cola_superheroes.size()):
        superhero = cola_superheroes.attention()
        if superhero.first_appearance < 1980:    #print de todos los villanos
            # print(superhero)
            pass
        
#E Listar los superheores que comienzan con  Bl, G, My, y W.
print()

for superhero in list_superhero:
    name = superhero.name
    if name.startswith(("Bl", "G", "My", "W")):
        # print(superhero)
        pass

#F Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
print()

list_superhero.add_criterion('real_name', order_by_real_name)
list_superhero.sort_by_criterion('real_name')
# list_superhero.show()

#G Listado de superheroes ordenados por fecha de aparación.
print()

list_superhero.add_criterion('first_appearance', order_by_first_appearance)
list_superhero.sort_by_criterion('first_appearance')
# list_superhero.show()

#H Modificar el nombre real de Ant Man a Scott Lang.
print()

index = list_superhero.search('Ant Man','name')
if index:
    list_superhero[index].name = 'Scott Lang'
else:
    print('el super heroe no esta en la lista')

#I Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit

for superhero in list_superhero:
    if 'time-traveling' in superhero.short_bio or 'suit' in superhero.short_bio:
        # print(superhero)
        pass
    
#J Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

hero = list_superhero.delete_value('Electro', 'name')
if hero:
    print(hero)

hero = list_superhero.delete_value('Baron Zemo', 'name')
if hero:
    print(hero)




