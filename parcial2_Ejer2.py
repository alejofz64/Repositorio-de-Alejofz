from grapf import Graph

g = Graph()

g.insert_vertex('Luke Skywalker')
g.insert_vertex('Darth Vader')
g.insert_vertex('Yoda')
g.insert_vertex('Boba Fett')
g.insert_vertex('Leia')
g.insert_vertex('C_3PO')
g.insert_vertex('Rey')
g.insert_vertex('Kylo Ren')
g.insert_vertex('Chewbacca')
g.insert_vertex('Han Solo')
g.insert_vertex('R2_D2')
g.insert_vertex('BB_8')


g.insert_edge('Luke Skywalker', 'Darth Vader', 5)
g.insert_edge('Luke Skywalker', 'Leia', 8)
g.insert_edge('Luke Skywalker', 'Han Solo', 7)
g.insert_edge('Luke Skywalker', 'Chewbacca', 6)
g.insert_edge('Luke Skywalker', 'C_3PO', 4)
g.insert_edge('Luke Skywalker', 'R2_D2', 6)
g.insert_edge('Luke Skywalker', 'Yoda', 3)
    
g.insert_edge('Darth Vader', 'Leia', 4)
g.insert_edge('Darth Vader', 'Luke Skywalker', 5)
g.insert_edge('Darth Vader', 'Yoda', 2)
    
g.insert_edge('Yoda', 'Luke Skywalker', 3)
g.insert_edge('Yoda', 'Darth Vader', 2)
g.insert_edge('Yoda', 'Leia', 2)
    
g.insert_edge('Leia', 'Luke Skywalker', 8)
g.insert_edge('Leia', 'Han Solo', 9)
g.insert_edge('Leia', 'Chewbacca', 7)
g.insert_edge('Leia', 'C_3PO', 6)
g.insert_edge('Leia', 'R2_D2', 5)
g.insert_edge('Leia', 'Darth Vader', 4)
    
g.insert_edge('Han Solo', 'Luke Skywalker', 7)
g.insert_edge('Han Solo', 'Leia', 9)
g.insert_edge('Han Solo', 'Chewbacca', 8)
g.insert_edge('Han Solo', 'C_3PO', 4)
g.insert_edge('Han Solo', 'R2_D2', 5)
    
g.insert_edge('Chewbacca', 'Luke Skywalker', 6)
g.insert_edge('Chewbacca', 'Han Solo', 8)
g.insert_edge('Chewbacca', 'Leia', 7)
    
g.insert_edge('C_3PO', 'R2_D2', 9)
g.insert_edge('C_3PO', 'Luke Skywalker', 4)
g.insert_edge('C_3PO', 'Leia', 6)
g.insert_edge('C_3PO', 'Han Solo', 4)
    
g.insert_edge('R2_D2', 'C_3PO', 9)
g.insert_edge('R2_D2', 'Luke Skywalker', 6)
g.insert_edge('R2_D2', 'Leia', 5)
g.insert_edge('R2_D2', 'Han Solo', 5)
    
g.insert_edge('Rey', 'Kylo Ren', 4)
g.insert_edge('Rey', 'BB_8', 3)
g.insert_edge('Rey', 'Leia', 2)
    
g.insert_edge('Kylo Ren', 'Rey', 4)
g.insert_edge('Kylo Ren', 'Leia', 3)
g.insert_edge('Kylo Ren', 'Han Solo', 2)
    
g.insert_edge('BB_8', 'Rey', 3)
g.insert_edge('BB_8', 'R2_D2', 2)
    
g.insert_edge('Boba Fett', 'Darth Vader', 3)
g.insert_edge('Boba Fett', 'Han Solo', 2)

g.show()
print()

#Punto A
print("Punto A")

personajes = ['C_3PO', 'Yoda', 'Leia']

for personaje in personajes:
    expansion_tree = g.kruskal(personaje)
    print(f"\nArbol de expansion minima desde {personaje}:")
    print(expansion_tree)
    
    peso_total = 0
    for edge in expansion_tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f'origin {origin} destination {destination}')
        peso_total += int(weight)
    print(f'peso total: {peso_total}')
    
print()
#Punto B
print("Punto B")

max_episodios = 0
pares_maximos = []

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight
            pares_maximos = [(vertex.value, edge.value)]
        elif edge.weight == max_episodios:
            # Evitar duplicados
            par = (vertex.value, edge.value)
            par_inverso = (edge.value, vertex.value)
            if par not in pares_maximos and par_inverso not in pares_maximos:
                pares_maximos.append(par)

print(f"Maximo numero de episodios compartidos: {max_episodios}")
print("Pares de personajes con este maximo:")
for par in pares_maximos:
    print(f"  {par[0]} - {par[1]}")

print()    
#Punto 3
print("Punto 3")
    
# Camino de C-3PO a R2-D2
print("Camino de C-3PO a R2-D2:")
path = g.dijkstra('C-3PO')
destination = 'R2-D2'
peso_total = None
camino_completo = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino_completo.append(value[0])
        destination = value[2]
camino_completo.reverse()
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

# Camino de Yoda a Darth Vader
print("\nCamino de Yoda a Darth Vader:")
path = g.dijkstra('Yoda')
destination = 'Darth Vader'
peso_total = None
camino_completo = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino_completo.append(value[0])
        destination = value[2]
camino_completo.reverse()
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

print()
#Punto 4
print("Punto 4")