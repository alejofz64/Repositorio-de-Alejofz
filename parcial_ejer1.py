#Ejercicio 1

superheroes = [
    "Spider-Man",
    "Iron Man",
    "Captain America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Doctor Strange",
    "Black Panther",
    "Wolverine",
]

def buscar_capitan_america(lista, indice=0):
    
    if indice >= len(lista):
        return False
    
    if lista[indice] == "Captain America":
        return True

    return buscar_capitan_america(lista, indice + 1)

def listar_superheroes(lista, indice=0):
  
    if indice >= len(lista):
        return None
    
    print(f"{indice + 1}. {lista[indice]}")
    
    listar_superheroes(lista, indice + 1)


if buscar_capitan_america(superheroes):
    print('El Capitan America esta en la lista')
else:
    print('EL Capitan America no esta en la lista')

listar_superheroes(superheroes)