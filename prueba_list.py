from list_ import List

class person:
    def __init__(self, nom, ape, dni):
        self.nom = nom
        self.ape = ape
        self.dni = dni
    
    def __str__(self):
        return f'{self.nom}, {self.ape} - {self.dni}'

people = [
    person(nom='Alejo',ape='Fernandez',dni=47),
    person(nom='Giuliana',ape='Galiani',dni=50),
    person(nom='Dana',ape='Cervin',dni=46),
    person(nom='Roman',ape='Olague',dni=49),
    person(nom='Maycol',ape='Banitez',dni=48) 
]

def order_by_name(item):
    return item.nom

def order_by_surname(item):
    return item.ape

def order_by_id(item):
    return item.dni


list_people = List()

list_people.add_criterion('nombre',order_by_name)

for person in people:
    list_people.append(person)


# list_people.show()


# print()
# print(list_people.search('Giuliana','nombre'))
# print()

list_people.sort_by_criterion('nombre')

print()
list_people.show()