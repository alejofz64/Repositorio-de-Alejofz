from superheroes_data2 import superheroes
from list_ import List

def order_by_name(item):
    return item.name

class Superhero:
    
    def __init__(self, name, short_bio, first_appearance, comic_house):
        self.name = name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.comic_house = comic_house
        
    def __str__(self):
        return f'{self.name}: {self.comic_house} ({self.first_appearance})'

list_superheroes = List()
list_superheroes.add_criterion('name', order_by_name)

for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        comic_house=superhero["comic_house"],
    )
    list_superheroes.append(hero)

#a. eliminar el nodo que contiene la información de Linterna Verde
print("a. Eliminar Linterna Verde:")
linterna_verde = list_superheroes.delete_value('Linterna Verde', 'name')
if linterna_verde:
    print(f"Se elimino: {linterna_verde}")
print()

# b. mostrar el año de aparición de Wolverine
print("b. Anio de aparicion de Wolverine:")
index = list_superheroes.search('Wolverine', 'name')
if index is not None:
    wolverine = list_superheroes[index]
    print(f"Wolverine aparecio en: {wolverine.first_appearance}")
else:
    print("wolverine no ha sido encontrado")
print()

# c. cambiar la casa de Dr. Strange a Marvel
print("c. Cambiar casa de Dr. Strange a Marvel:")
index = list_superheroes.search('Dr. Strange', 'name')
if index is not None:
    list_superheroes[index].comic_house = "Marvel"
print()

# d. mostrar el nombre de aquellos superheroes que en su biografía menciona la palabra "traje" o "armadura"
print("d. Superheroes con 'traje' o 'armadura' en su biografia:")
for hero in list_superheroes:
    if 'traje' in hero.short_bio.lower() or 'armadura' in hero.short_bio.lower():
        print(hero.name)
print()

# e. mostrar el nombre y la casa de los superheroes cuya fecha de aparicion sea anterior a 1963
print("e. Superheroes con aparicion anterior a 1963:")
for hero in list_superheroes:
    if hero.first_appearance < 1963:
        print(f"{hero.name} - {hero.comic_house}")
print()

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
print("f. Casas de Capitana Marvel y Mujer Maravilla:")
index = list_superheroes.search('Capitana Marvel', 'name')
if index is not None:
    print(f"Capitana Marvel: {list_superheroes[index].comic_house}")

index = list_superheroes.search('Mujer Maravilla', 'name')
if index is not None:
    print(f"Mujer Maravilla: {list_superheroes[index].comic_house}")
print()

# g. mostrar toda la información de Flash y Star-Lord
print("g. Informacion completa de Flash y Star-Lord:")
index = list_superheroes.search('Flash', 'name')
if index is not None:
    flash = list_superheroes[index]
    print(f"Flash: {flash}")

index = list_superheroes.search('Star-Lord', 'name')
if index is not None:
    star_lord = list_superheroes[index]
    print(f"Star-Lord: {star_lord}")
print()

# h. listar los superhéroes que comienzan con la letra B, M y S
print("h. Superheroes que comienzan con B, M y S:")
letras = ['B', 'M', 'S']
for letra in letras:
    print(f"Con {letra}:")
    for hero in list_superheroes:
        if hero.name.startswith(letra):
            print(f"  {hero.name}")
print()

# i. determinar cuántos superhéroes hay de cada casa de comic
print("i. Cantidad de superheroes por casa de comic:")

cont_Marvel = 0
cont_DC = 0
for hero in list_superheroes:
    casa = hero.comic_house
    if casa == "Marvel":
        cont_Marvel += 1
    else:
        cont_DC += 1
print(f"Marvel: {cont_Marvel} superheroes")
print(f"DC: {cont_DC} superheroes")
