from grapf import Graph

g = Graph() 


# PCs
g.insert_vertex('Manjaro', 'pc')
g.insert_vertex('Fedora', 'pc')
g.insert_vertex('Mint', 'pc')
g.insert_vertex('Parrot', 'pc')
g.insert_vertex('Ubuntu', 'pc')

# Notebooks
g.insert_vertex('Debian', 'notebook')
g.insert_vertex('Arch', 'notebook')
g.insert_vertex('Red Hat', 'notebook')

# Servidores
g.insert_vertex('Guarani', 'servidor')
g.insert_vertex('MongoDB', 'servidor')

# Routers
g.insert_vertex('Router 1', 'router')
g.insert_vertex('Router 2', 'router')
g.insert_vertex('Router 3', 'router')

# Switches
g.insert_vertex('Switch 1', 'switch')
g.insert_vertex('Switch 2', 'switch')

# Impresora
g.insert_vertex('Impresora', 'impresora')



g.insert_edge('Guarani', 'Router 2', 2)

g.insert_edge('Router 2', 'Red Hat', 25)
g.insert_edge('Router 2', 'Router 3', 50)

g.insert_edge('Router 1', 'Router 3', 43)
g.insert_edge('Router 1', 'Router 2', 37)
g.insert_edge('Router 1', 'Switch 1', 29)

g.insert_edge('Switch 1', 'Debian', 17)
g.insert_edge('Switch 1', 'Ubuntu', 18)
g.insert_edge('Switch 1', 'Impresora', 22)
g.insert_edge('Switch 1', 'Mint', 80)

g.insert_edge('Switch 2', 'Router 3', 61)
g.insert_edge('Switch 2', 'Manjaro', 40)
g.insert_edge('Switch 2', 'Parrot', 12)
g.insert_edge('Switch 2', 'MongoDB', 5)
g.insert_edge('Switch 2', 'Arch', 56)
g.insert_edge('Switch 2', 'Fedora', 3)



# #B
# print('=== PUNTO B ===')
# print("Barrido por amplitud")
# notebooks = ['Red Hat', 'Debian','Arch']
# for notebook in notebooks:
#     print(f"    Barrido de {notebook} ")
#     g.amplitude_sweep(notebook)
#     print()

# print("Barrido por profundidad")
# print()
notebooks = ['Red Hat', 'Debian','Arch']
# for notebook in notebooks:
#     print(f"    Barrido de {notebook} ")
#     g.deep_sweep(notebook)
#     print()
    
# #C
# print("=== PUNTO C ===")
# pcs_impresion = ['Manjaro', 'Red Hat', 'Fedora']
# for pc in pcs_impresion:
#     print(f"Camino mas corto desde {pc} hasta Impresora:")
#     path = g.dijkstra(pc)
#     destination = 'Impresora'
#     peso_total = None
#     camino_completo = []

#     while path.size() > 0:
#         value = path.pop()
#         if value[0] == destination:
#             if peso_total is None:
#                 peso_total = value[1]
#             camino_completo.append(value[0])
#             destination = value[2]
#     camino_completo.reverse()
#     if camino_completo:
#         print(f'  Camino: {"-".join(camino_completo)} con costo: {peso_total}')
#     else:
#         print(f'  No hay camino desde {pc} hasta Impresora')
#     print()

# #D
# print("=== PUNTO D ===")
# expansion_tree = g.kruskal('Router 1')
# print(f"Arbol de expansion minima: {expansion_tree}")

# # Calcular peso total
# peso_total = 0
# if ';' in expansion_tree:
#     for edge in expansion_tree.split(';'):
#         parts = edge.split('-')
#         if len(parts) >= 3:
#             peso_total += int(parts[2])
# else:
#     parts = expansion_tree.split('-')
#     if len(parts) >= 3:
#         peso_total = int(parts[2])

# print(f'Peso total del arbol de expansion minima: {peso_total}')
# print()

# #E
# print("=== PUNTO E ===")
# pcs = ['Manjaro', 'Fedora', 'Mint', 'Parrot', 'Ubuntu']
# mejor_pc = None
# mejor_camino = None
# mejor_costo = float('inf')

# for pc in pcs:
#     path = g.dijkstra(pc)
#     destination = 'Guarani'
#     peso_total = None
#     camino_completo = []

#     while path.size() > 0:
#         value = path.pop()
#         if value[0] == destination:
#             if peso_total is None:
#                 peso_total = value[1]
#             camino_completo.append(value[0])
#             destination = value[2]
#     camino_completo.reverse()
    
#     if camino_completo and peso_total is not None and peso_total < mejor_costo:
#         mejor_costo = peso_total
#         mejor_pc = pc
#         mejor_camino = camino_completo

# if mejor_pc:
#     print(f"La PC con el camino mas corto a Guarani es: {mejor_pc}")
#     print(f"Camino: {'-'.join(mejor_camino)}")
#     print(f"Costo: {mejor_costo}")
# else:
#     print("No se encontro camino desde ninguna PC al servidor Guarani")
# print()

# #F
# print("=== PUNTO F ===")
# # Las computadoras conectadas al Switch 1 son: Debian, Ubuntu, Mint
# computadoras_switch1 = ['Debian', 'Ubuntu', 'Mint']
# mejor_computadora = None
# mejor_camino_f = None
# mejor_costo_f = float('inf')

# for comp in computadoras_switch1:
#     path = g.dijkstra(comp)
#     destination = 'MongoDB'
#     peso_total = None
#     camino_completo = []

#     while path.size() > 0:
#         value = path.pop()
#         if value[0] == destination:
#             if peso_total is None:
#                 peso_total = value[1]
#             camino_completo.append(value[0])
#             destination = value[2]
#     camino_completo.reverse()
    
#     if camino_completo and peso_total is not None and peso_total < mejor_costo_f:
#         mejor_costo_f = peso_total
#         mejor_computadora = comp
#         mejor_camino_f = camino_completo

# if mejor_computadora:
#     print(f"La computadora del Switch 1 con el camino mas corto a MongoDB es: {mejor_computadora}")
#     print(f"Camino: {'-'.join(mejor_camino_f)}")
#     print(f"Costo: {mejor_costo_f}")
# else:
#     print("No se encontro camino desde ninguna computadora del Switch 1 al servidor MongoDB")
# print()

#G
print("=== PUNTO G ===")
print("Cambiando conexion de Impresora al Router 2...")


g.delete_edge('Switch 1', 'Impresora','value')

# Agregar nueva conexión al Router 2
g.insert_edge('Impresora', 'Router 2', 15)

print("Nuevo barrido por amplitud despues del cambio:")
for notebook in notebooks:
    print(f"    Barrido de {notebook}:")
    g.amplitude_sweep(notebook)
    print()

print("Nuevo barrido por profundidad despues del cambio:")
for notebook in notebooks:
    print(f"    Barrido de {notebook}:")
    g.deep_sweep(notebook)
    print()