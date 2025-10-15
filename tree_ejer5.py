from tree import BinaryTree

# Crear el arbol principal
superheroes_villanos = BinaryTree()

# Cargar personajes del MCU
personajes = [
    ('Iron Man', {'is_villain': False}),
    ('Captain America', {'is_villain': False}),
    ('Thor', {'is_villain': False}),
    ('Loki', {'is_villain': True}),
    ('Thanos', {'is_villain': True}),
    ('Black Widow', {'is_villain': False}),
    ('Dr Strnge', {'is_villain': False}),  # Mal escrito a proposito
    ('Spider-Man', {'is_villain': False}),
    ('Black Panther', {'is_villain': False}),
    ('Captain Marvel', {'is_villain': False}),
    ('Ant-Man', {'is_villain': False}),
    ('Wasp', {'is_villain': False}),
    ('Scarlet Witch', {'is_villain': False}),
    ('Vision', {'is_villain': False}),
    ('Falcon', {'is_villain': False}),
    ('Winter Soldier', {'is_villain': False}),
    ('Star-Lord', {'is_villain': False}),
    ('Gamora', {'is_villain': False}),
    ('Rocket Raccoon', {'is_villain': False}),
    ('Groot', {'is_villain': False}),
    ('Drax', {'is_villain': False}),
    ('Cable', {'is_villain': False}),
    ('Cyclops', {'is_villain': False}),
    ('Red Skull', {'is_villain': True}),
    ('Ultron', {'is_villain': True}),
    ('Baron Zemo', {'is_villain': True}),
    ('Ronan', {'is_villain': True}),
    ('Ego', {'is_villain': True}),
    ('Hela', {'is_villain': True}),
    ('Killmonger', {'is_villain': True}),
    ('Vulture', {'is_villain': True}),
    ('Mysterio', {'is_villain': True}),
    ('Green Goblin', {'is_villain': True}),
    ('Doctor Octopus', {'is_villain': True}),
    ('Carnage', {'is_villain': True}),
    ('Magneto', {'is_villain': True}),
]

for nombre, info in personajes:
    superheroes_villanos.insert(nombre, info)

print("Arbol completo del MCU:")
superheroes_villanos.in_order()
print()

# b. listar los villanos ordenados alfabeticamente
print("b. Villanos ordenados alfabeticamente:")
def listar_villanos(root):
    if root is not None:
        listar_villanos(root.left)
        if root.other_values['is_villain']:
            print(f"  - {root.value}")
        listar_villanos(root.right)

listar_villanos(superheroes_villanos.root)
print()

# c. mostrar todos los superheroes que empiezan con C
print("c. Superheroes que empiezan con C:")
def superheroes_con_C(root):
    if root is not None:
        superheroes_con_C(root.left)
        if not root.other_values['is_villain'] and root.value.startswith('C'):
            print(f"  - {root.value}")
        superheroes_con_C(root.right)

superheroes_con_C(superheroes_villanos.root)
print()

# d. determinar cuantos superheroes hay el arbol
print("d. Cantidad de superheroes:")
def contar_superheroes(root):
    if root is None:
        return 0
    count = 0
    if not root.other_values['is_villain']:
        count = 1
    return count + contar_superheroes(root.left) + contar_superheroes(root.right)

total_heroes = contar_superheroes(superheroes_villanos.root)
print(f"  Total de superheroes: {total_heroes}")
print()

# e. Doctor Strange en realidad esta mal cargado. Utilice una busqueda por proximidad
print("e. Correccion de Doctor Strange usando busqueda por proximidad:")
print("  Buscando personajes que empiezan con 'Dr':")
superheroes_villanos.proximity_search('Dr')

name = input('ingrese nombre para modificar: ')
value, other_value = superheroes_villanos.delete(name)

if value is not None:
    fix_name = input('ingrese el nuevo nombre: ')
    superheroes_villanos.insert(fix_name, other_value)
else:
    print("  ✗ Personaje no encontrado")
print()

# f. listar los superheroes ordenados de manera descendente
print("f. Superheroes ordenados descendente:")
def superheroes_descendente(root):
    if root is not None:
        superheroes_descendente(root.right)
        if not root.other_values['is_villain']:
            print(f"  - {root.value}")
        superheroes_descendente(root.left)

superheroes_descendente(superheroes_villanos.root)
print()

# g. generar un bosque a partir de este arbol
print("g. Generacion del bosque")
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def dividir_arbol(root, arbol_h, arbol_v):
    if root is not None:
        dividir_arbol(root.left, arbol_h, arbol_v)
        if not root.other_values['is_villain']:
            arbol_h.insert(root.value, root.other_values)
        else:
            arbol_v.insert(root.value, root.other_values)
        dividir_arbol(root.right, arbol_h, arbol_v)

dividir_arbol(superheroes_villanos.root, arbol_heroes, arbol_villanos)

# g.I. determinar cuantos nodos tiene cada arbol
print("g.I. Nodos por arbol:")
def contar_nodos(root):
    if root is None:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)

nodos_heroes = contar_nodos(arbol_heroes.root)
nodos_villanos = contar_nodos(arbol_villanos.root)
print(f"  Arbol de heroes: {nodos_heroes} nodos")
print(f"  Arbol de villanos: {nodos_villanos} nodos")
print(f"  Total: {nodos_heroes + nodos_villanos} nodos")
print()

# g.II. realizar un barrido ordenado alfabeticamente de cada arbol
print("g.II. Barrido alfabetico - Heroes:")
arbol_heroes.in_order()
print()

print("g.II. Barrido alfabetico - Villanos:")
arbol_villanos.in_order()
print()

# Verificacion final
print("Verificacion - Arbol completo despues de correcciones:")
superheroes_villanos.in_order()

