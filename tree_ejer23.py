from tree import BinaryTree

criaturas_tree = BinaryTree()

criaturas_data = [
    ('Ceto', {'derrotado_por': '-'}),
    ('Tifon', {'derrotado_por': 'Zeus'}),
    ('Equidna', {'derrotado_por': 'Argos Panoptes'}),
    ('Dino', {'derrotado_por': '-'}),
    ('Pefredo', {'derrotado_por': '-'}),
    ('Enio', {'derrotado_por': '-'}),
    ('Escila', {'derrotado_por': '-'}),
    ('Caribdis', {'derrotado_por': '-'}),
    ('Euriale', {'derrotado_por': '-'}),
    ('Esteno', {'derrotado_por': '-'}),
    ('Medusa', {'derrotado_por': 'Perseo'}),
    ('Ladon', {'derrotado_por': 'Heracles'}),
    ('Aguila del Caucaso', {'derrotado_por': '-'}),
    ('Quimera', {'derrotado_por': 'Belerofonte'}),
    ('Hidra de Lerna', {'derrotado_por': 'Heracles'}),
    ('Leon de Nemea', {'derrotado_por': 'Heracles'}),
    ('Esfinge', {'derrotado_por': 'Edipo'}),
    ('Dragon de la Colquida', {'derrotado_por': '-'}),
    ('Cerbero', {'derrotado_por': '-'}),
    ('Cerda de Cromion', {'derrotado_por': 'Tesco'}),
    ('Ortro', {'derrotado_por': 'Heracles'}),
    ('Toro de Creta', {'derrotado_por': 'Tesco'}),
    ('Jabalí de Calidon', {'derrotado_por': 'Atalanta'}),
    ('Carcinos', {'derrotado_por': '-'}),
    ('Gerion', {'derrotado_por': 'Heracles'}),
    ('Cloto', {'derrotado_por': '-'}),
    ('Laquesis', {'derrotado_por': '-'}),
    ('Atropos', {'derrotado_por': '-'}),
    ('Minotauro de Creta', {'derrotado_por': 'Tesco'}),
    ('Harpías', {'derrotado_por': '-'}),
    ('Argos Panoptes', {'derrotado_por': 'Hermes'}),
    ('Aves del Estínfalo', {'derrotado_por': '-'}),
    ('Talos', {'derrotado_por': 'Medea'}),
    ('Sirenas', {'derrotado_por': '-'}),
    ('Piton', {'derrotado_por': 'Apolo'}),
    ('Cierva de Cerinea', {'derrotado_por': '-'}),
    ('Basilisco', {'derrotado_por': '-'}),
    ('Jabalí de Erimanto', {'derrotado_por': '-'}),
]

for criatura, info in criaturas_data:
    info['capturada'] = ''
    info['descripcion'] = ''
    criaturas_tree.insert(criatura, info)

print("Arbol de criaturas mitologicas cargado exitosamente!")
print()

# a. listado inorden de las criaturas y quienes la derrotaron
print("a. Listado inorden de criaturas y sus vencedores:")
criaturas_tree.in_order()
print()

# b. se debe permitir cargar una breve descripcion sobre cada criatura
print("b. Cargar descripciones (ejemplo para algunas criaturas):")
def cargar_descripciones():
    descripciones = {
        'Talos': 'Gigante de bronce que protegía la isla de Creta, derrotado por Medea',
        'Cerbero': 'Perro de tres cabezas que guardaba la entrada al Inframundo',
        'Medusa': 'Criatura femenina con serpientes en lugar de cabello, podia petrificar con la mirada',
        'Quimera': 'Monstruo que escupia fuego, con cabeza de leon, cuerpo de cabra y cola de serpiente'
    }
    
    for nombre, desc in descripciones.items():
        nodo = criaturas_tree.search(nombre)
        if nodo is not None:
            nodo.other_values['descripcion'] = desc
            print(f"  Descripcion cargada para {nombre}")

cargar_descripciones()
print()

# c. mostrar toda la informacion de la criatura Talos
print("c. Informacion completa de Talos:")
talos_node = criaturas_tree.search('Talos')
if talos_node is not None:
    print(f"  Nombre: {talos_node.value}")
    print(f"  Derrotado por: {talos_node.other_values['derrotado_por']}")
    print(f"  Capturada por: {talos_node.other_values['capturada']}")
    print(f"  Descripcion: {talos_node.other_values['descripcion']}")
else:
    print("  Talos no encontrado")
print()

# d. determinar los 3 heroes o dioses que derrotaron mayor cantidad de criaturas
print("d. Top 3 heroes/dioses que derrotaron ms criaturas:")
def top_3_vencedores(root):
    ranking = {}
    
    def contar_vencedores(node):
        if node is not None:
            contar_vencedores(node.left)
            vencedor = node.other_values['derrotado_por']
            if vencedor != '-':
                if vencedor not in ranking:
                    ranking[vencedor] = 0
                ranking[vencedor] += 1
            contar_vencedores(node.right)
    
    contar_vencedores(root)
    
    vencedores_ordenados = []
    for heroe, cantidad in ranking.items():
        vencedores_ordenados.append((cantidad, heroe))

    vencedores_ordenados.sort(reverse=True)
    
    print("  Ranking de heroes:")
    
    print("     ",vencedores_ordenados[0])
    print("     ",vencedores_ordenados[1])
    print("     ",vencedores_ordenados[2])
    

top_3_vencedores(criaturas_tree.root)
print()

# e. listar las criaturas derrotadas por Heracles
print("e. Criaturas derrotadas por Heracles:")
def criaturas_de_heracles(root):
    if root is not None:
        criaturas_de_heracles(root.left)
        if root.other_values['derrotado_por'] == 'Heracles':
            print(f"  - {root.value}")
        criaturas_de_heracles(root.right)

criaturas_de_heracles(criaturas_tree.root)
print()

# f. listar las criaturas que no han sido derrotadas
print("f. Criaturas no derrotadas:")
def criaturas_no_derrotadas(root):
    if root is not None:
        criaturas_no_derrotadas(root.left)
        if root.other_values['derrotado_por'] == '-':
            print(f"  - {root.value}")
        criaturas_no_derrotadas(root.right)

criaturas_no_derrotadas(criaturas_tree.root)
print()

# g. campo "capturada" ya fue agregado en la carga inicial

# h. modificar criaturas capturadas por Heracles
print("h. Marcando criaturas capturadas por Heracles:")
criaturas_heracles = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']

for criatura in criaturas_heracles:
    nodo = criaturas_tree.search(criatura)
    if nodo is not None:
        nodo.other_values['capturada'] = 'Heracles'
        print(f"  ✓ {criatura} capturada por Heracles")
print()

# i. se debe permitir busquedas por coincidencia
print("i. Busqueda por coincidencia 'Dragon':")
criaturas_tree.proximity_search('Dragon')
print()

# j. eliminar al Basilisco y a las Sirenas
print("j. Eliminando Basilisco y Sirenas:")
criaturas_a_eliminar = ['Basilisco', 'Sirenas']

for criatura in criaturas_a_eliminar:
    value, other_value = criaturas_tree.delete(criatura)
    if value is not None:
        print(f"   {criatura} eliminado")
    else:
        print(f"   {criatura} no encontrado")
print()

# k. modificar Aves del Estínfalo
print("k. Modificando Aves del Estínfalo:")
aves_node = criaturas_tree.search('Aves del Estínfalo')
if aves_node is not None:
    aves_node.other_values['derrotado_por'] = 'Heracles (varias)'
    aves_node.other_values['descripcion'] = 'Aves carnívoras derrotadas por Heracles en uno de sus trabajos'
    print("   Aves del Estínfalo modificadas")
print()

# l. modificar nombre de Ladon por Dragon Ladon
print("l. Modificando nombre de Ladon:")
ladon_value, ladon_other = criaturas_tree.delete('Ladon')
if ladon_value is not None:
    criaturas_tree.insert('Dragon Ladon', ladon_other)
    print("   Ladon renombrado a Dragon Ladon")
print()

# m. realizar un listado por nivel del arbol
print("m. Listado por nivel del arbol:")
criaturas_tree.by_level()
print()

# n. mostrar las criaturas capturadas por Heracles
print("n. Criaturas capturadas por Heracles:")
def criaturas_capturadas_heracles(root):
    if root is not None:
        criaturas_capturadas_heracles(root.left)
        if root.other_values['capturada'] == 'Heracles':
            print(f"  - {root.value}")
        criaturas_capturadas_heracles(root.right)

criaturas_capturadas_heracles(criaturas_tree.root)

# Verificacion final
print("\n" + "="*50)
print("VERIFICACION FINAL - Arbol actualizado:")
print("="*50)
criaturas_tree.in_order()