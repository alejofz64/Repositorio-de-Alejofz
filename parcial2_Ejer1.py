from tree import BinaryTree

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

pokemons = [
    (1, 'Bulbasaur', ['Planta', 'Veneno'], ['Fuego', 'Psiquico', 'Volador', 'Hielo'], False, False),
    (4, 'Charmander', ['Fuego'], ['Agua', 'Tierra', 'Roca'], False, False),
    (7, 'Squirtle', ['Agua'], ['Planta', 'Electrico'], False, False),
    (25, 'Pikachu', ['Electrico'], ['Tierra'], False, True),
    (26, 'Raichu', ['Electrico'], ['Tierra'], False, False),
    (94, 'Gengar', ['Fantasma', 'Veneno'], ['Fantasma', 'Siniestro', 'Psiquico'], True, False),
    (135, 'Jolteon', ['Electrico'], ['Tierra'], False, False),
    (150, 'Mewtwo', ['Psiquico'], ['Fantasma', 'Bicho', 'Siniestro'], True, False),
    (151, 'Mew', ['Psiquico'], ['Fantasma', 'Bicho', 'Siniestro'], False, False),
    (212, 'Scizor', ['Bicho', 'Acero'], ['Fuego'], True, False),
    (306, 'Aggron', ['Acero', 'Roca'], ['Lucha', 'Tierra', 'Agua'], True, False),
    (448, 'Lucario', ['Lucha', 'Acero'], ['Fuego', 'Lucha', 'Tierra'], True, False),
    (6, 'Charizard', ['Fuego', 'Volador'], ['Agua', 'Electrico', 'Roca'], True, True),
    (9, 'Blastoise', ['Agua'], ['Planta', 'Electrico'], True, True),
    (3, 'Venusaur', ['Planta', 'Veneno'], ['Fuego', 'Psiquico', 'Volador', 'Hielo'], True, False),
    (745, 'Lycanroc', ['Roca'], ['Agua', 'Planta', 'Lucha', 'Tierra', 'Acero'], False, False),
    (697, 'Tyrantrum', ['Roca', 'Dragon'], ['Hielo', 'Hada', 'Lucha', 'Acero', 'Dragon'], False, False),
    (130, 'Gyarados', ['Agua', 'Volador'], ['Electrico', 'Roca'], True, True),
    (380, 'Latias', ['Dragon', 'Psiquico'], ['Hielo', 'Fantasma', 'Siniestro', 'Hada', 'Bicho', 'Dragon'], True, False),
    (381, 'Latios', ['Dragon', 'Psiquico'], ['Hielo', 'Fantasma', 'Siniestro', 'Hada', 'Bicho', 'Dragon'], True, False),
]

for numero, nombre, tipos, debilidades, mega_evolucion, gigamax in pokemons:
    datos_pokemon = {
        'numero': numero,
        'nombre': nombre,
        'tipos': tipos,
        'debilidades': debilidades,
        'mega_evolucion': mega_evolucion,
        'gigamax': gigamax
    }
    arbol_nombre.insert(nombre, datos_pokemon)
    arbol_numero.insert(numero, datos_pokemon)
    for tipo in tipos:
        arbol_tipo.insert(tipo, datos_pokemon)



# a. mostrar todos los datos de un Pokemon a partir de su numero y nombre
print("a")
print("   Buscando Pokemon numero 25:")
nodo = arbol_numero.search(25)
if nodo:
    datos = nodo.other_values
    print(f"   {datos['numero']}: {datos['nombre']}")
    print(f"   Tipos: {', '.join(datos['tipos'])}")
    print(f"   Debilidades: {', '.join(datos['debilidades'])}")
    print(f"   Mega Evolucion: {'Si' if datos['mega_evolucion'] else 'No'}")
    print(f"   Gigamax: {'Si' if datos['gigamax'] else 'No'}")

#Por proximidad y nomre
def buscar_por_proximidad(root, texto):
    def __buscar(root, texto):
        if root is not None:
            if root.value.startswith(texto):
                print(f"   - {root.value} (#{root.other_values['numero']})")
            __buscar(root.left, texto)
            __buscar(root.right, texto)
    
    if root is not None:
        __buscar(root, texto)
print("Busqueda por proximidad 'Char'")
buscar_por_proximidad(arbol_nombre.root, 'Char')
print()

# b. mostrar todos los nombres de los Pokemons de tipos especificos
print("b. Pokemons por tipo:")
tipos_buscar = ['Fantasma', 'Fuego', 'Acero', 'Electrico']

for tipo in tipos_buscar:
    print(f"   {tipo}:")
    def mostrar_por_tipo(root, tipo_buscar):
        if root is not None:
            mostrar_por_tipo(root.left, tipo_buscar)
            if root.value == tipo_buscar:
                datos = root.other_values
                print(f"     - {datos['nombre']} ({datos['numero']})")
            mostrar_por_tipo(root.right, tipo_buscar)
    
    mostrar_por_tipo(arbol_tipo.root, tipo)
print()

# c. listado en orden ascendente por numero y nombre
print("c. Listados ordenados:")
print("Orden ascendente por numero:")
# arbol_numero.in_order()
print()
print("Orden ascendente por nombre:")
# arbol_nombre.in_order()
print()
print("listado por nivel con nombre")
# arbol_nombre.by_level()
print()

# d. mostrar Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum
print("d. Pokemons debiles frente a Jolteon, Lycanroc y Tyrantrum:")

def mostrar_debiles():
    tipos_objetivo = ["Eléctrico", "Roca", "Dragón"]
    
    def __mostrar_debiles(root):
        if root is not None:
            __mostrar_debiles(root.left)
            # Verificar si AL MENOS UNA debilidad está en tipos_objetivo
            debilidades_pokemon = root.other_values["debilidades"]
            if any(debilidad in tipos_objetivo for debilidad in debilidades_pokemon):
                datos = root.other_values
                print(f"  - {datos['nombre']} ({datos['numero']})")
            __mostrar_debiles(root.right)

    if arbol_nombre.root is not None:
        __mostrar_debiles(arbol_nombre.root)
        
mostrar_debiles()



# e. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo
print("e. Conteo de Pokemons por tipo:")
contador_tipos = {}

def contar_por_tipo(root):
    if root is not None:
        contar_por_tipo(root.left)
        tipo = root.value
        if tipo not in contador_tipos:
            contador_tipos[tipo] = 0
        contador_tipos[tipo] += 1
        contar_por_tipo(root.right)

contar_por_tipo(arbol_tipo.root)

for tipo, cantidad in contador_tipos.items():
    print(f"   {tipo}: {cantidad} ")
print()



# f. determinar cuántos Pokémons tienen megaevolución
print("f. Pokemons con megaevolucion:")

def count_megaevolucion(self):
    def __count_megaevolucion(root):
        count = 0
        if root is not None:
            if root.other_values["mega_evolucion"] is True:
                count += 1
            count += __count_megaevolucion(root.left)
            count += __count_megaevolucion(root.right)

        return count
    
    total = 0
    if self.root is not None:
        total = __count_megaevolucion(self.root)

    return total

total=count_megaevolucion(arbol_nombre)
print (f"La cantidad de pokemos con megaevolucion son: {total}")


# g. determinar cuántos Pokémons tienen forma gigamax
print("g. Pokemons con forma gigamax:")
def count_gigamax(self):
    def __count_gigamax(root):
        count = 0
        if root is not None:
            if root.other_values["mega_evolucion"] is True:
                count += 1
            count += __count_gigamax(root.left)
            count += __count_gigamax(root.right)

        return count
    
    total = 0
    if self.root is not None:
        total = __count_gigamax(self.root)

    return total

total=count_megaevolucion(arbol_nombre)
print (f"La cantidad de pokemos con forma gigamax son: {total}")
