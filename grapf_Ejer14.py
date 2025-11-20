from grapf import Graph

g = Graph()

ambientes = [
    'cocina', 'comedor', 'cochera', 'quincho', 'banio 1', 'banio 2', 'habitacion 1', 'habitacion 2', 
    'sala de estar', 'terraza', 'patio'
]

for ambiente in ambientes:
    g.insert_vertex(ambiente)


g.insert_edge('cocina', 'comedor', 5)
g.insert_edge('cocina', 'patio', 8)
g.insert_edge('cocina', 'sala de estar', 6)


g.insert_edge('comedor', 'sala de estar', 4)
g.insert_edge('comedor', 'terraza', 7)
g.insert_edge('comedor', 'patio', 3)


g.insert_edge('cochera', 'patio', 10)
g.insert_edge('cochera', 'quincho', 6)
g.insert_edge('cochera', 'habitacion 1', 12)
g.insert_edge('cochera', 'habitacion 2', 15)
g.insert_edge('cochera', 'banio 1', 8)


g.insert_edge('quincho', 'patio', 4)
g.insert_edge('quincho', 'terraza', 5)
g.insert_edge('quincho', 'banio 2', 7)
g.insert_edge('quincho', 'habitacion 2', 9)
g.insert_edge('quincho', 'comedor', 8)


g.insert_edge('banio 1', 'habitacion 1', 3)
g.insert_edge('banio 1', 'habitacion 2', 6)
g.insert_edge('banio 1', 'sala de estar', 7)


g.insert_edge('banio 2', 'habitacion 2', 4)
g.insert_edge('banio 2', 'terraza', 6)
g.insert_edge('banio 2', 'patio', 5)


g.insert_edge('habitacion 1', 'sala de estar', 5)
g.insert_edge('habitacion 1', 'habitacion 2', 4)
g.insert_edge('habitacion 1', 'banio 1', 3)


g.insert_edge('habitacion 2', 'terraza', 8)
g.insert_edge('habitacion 2', 'patio', 7)
g.insert_edge('habitacion 2', 'banio 2', 4)


g.insert_edge('sala de estar', 'patio', 6)
g.insert_edge('sala de estar', 'terraza', 9)
g.insert_edge('sala de estar', 'comedor', 4)


g.insert_edge('terraza', 'patio', 2)
g.insert_edge('terraza', 'quincho', 5)
g.insert_edge('terraza', 'comedor', 7)


g.insert_edge('patio', 'terraza', 2)
g.insert_edge('patio', 'quincho', 4)
g.insert_edge('patio', 'cochera', 10)


# #C
# print("=== PUNTO c ===")
# print("Arbol de expansion minima para conectar todos los ambientes:")

# expansion_tree = g.kruskal('cocina')
# print(f"Arbol: {expansion_tree}")


# metros_totales = 0
# if ';' in expansion_tree:
#     for edge in expansion_tree.split(';'):
#         parts = edge.split('-')
#         if len(parts) >= 3:
#             metros_totales += int(parts[2])
# else:
#     parts = expansion_tree.split('-')
#     if len(parts) >= 3:
#         metros_totales = int(parts[2])

# print(f"Se necesitan {metros_totales} metros de cable para conectar todos los ambientes")
# print()

#D
print("=== PUNTO D ===")
print("Camino mas corto desde habitacion 1 hasta sala de estar (para cable de red):")

path = g.dijkstra('habitacion 1')
destination = 'sala de estar'
metros_cable_red = None
camino_completo = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if metros_cable_red is None:
            metros_cable_red = value[1]
        camino_completo.append(value[0])
        destination = value[2]
camino_completo.reverse()

if camino_completo:
    print(f"Camino: {' -> '.join(camino_completo)}")
    print(f"Se necesitan {metros_cable_red} metros de cable de red")
    print("(Para conectar el router en habitacion 1 con el Smart TV en sala de estar)")
else:
    print("No hay camino disponible entre habitacion 1 y sala de estar")
print()
