#Autor: Patricio Vega Mondaca 
#Ramo: Tecnicas de busqueda y Heuristicas, Diplomado en Int. Artificial 2023.
from collections import deque

# Representación del grafo como un diccionario de listas de adyacencia
grafo = {
    'UAI-Las Condes': ['El Golf', 'Vitacura', 'La Reina'],
    'El Golf': ['UAI-Las Condes', 'Vitacura'],
    'Vitacura': ['UAI-Las Condes', 'El Golf', 'La Reina', 'Lo Barnechea'],
    'La Reina': ['UAI-Las Condes', 'Vitacura', 'Ñuñoa'],
    'Lo Barnechea': ['Vitacura', 'La Dehesa'],
    'Ñuñoa': ['La Reina', 'Providencia'],
    'La Dehesa': ['Lo Barnechea'],
    'Providencia': ['Ñuñoa', 'Santiago Centro'],
    'Santiago Centro': ['Providencia', 'Independencia', 'San Miguel'],
    'Independencia': ['Santiago Centro', 'Renca'],
    'Renca': ['Independencia'],
    'San Miguel': ['Santiago Centro', 'La Cisterna'],
    'La Cisterna': ['San Miguel','La Granja','Lo Espejo'],
    'La Granja': ['La Cisterna', 'La Florida'],
    'La Florida': ['La Granja'],
    'Lo Espejo': ['La Cisterna', 'San Miguel'],
}

def bfs(grafo, nodo_inicial, objetivo_nodos, max_nodos=20):
    # Inicializar el conjunto de nodos visitados
    visitados = set()
    
    # Crear una cola para el recorrido BFS y agregar el nodo inicial con su camino y nivel
    cola = deque([(nodo_inicial, [nodo_inicial], 0)])
    
    # Inicializar el nivel actual
    nivel_actual = 0
    
    # Lista para almacenar el orden del recorrido
    orden_recorrido = []
    
    # Marcar el nodo inicial como visitado
    visitados.add(nodo_inicial)

    # Añadir el nodo inicial al orden de recorrido con nivel 0 y distancia 0
    orden_recorrido.append((nodo_inicial, 0, 0))

    # Comenzar el recorrido BFS
    while cola:
        # Desencolar el nodo actual, su camino y nivel
        nodo, camino, nivel = cola.popleft()

        # Actualizar el nivel actual si el nivel del nodo actual es mayor
        if nivel > nivel_actual:
            nivel_actual = nivel

        # Verificar si se ha alcanzado el número máximo de nodos permitidos
        if nivel_actual < max_nodos:
            # Explorar los vecinos del nodo actual en el grafo
            for vecino in grafo[nodo]:
                # Si el vecino no ha sido visitado previamente, agregarlo a la cola
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino], nivel + 1))  # Agregar vecino a la cola
                    visitados.add(vecino)  # Marcar el vecino como visitado
                    distancia_recorrida = len(camino)  # Calcular la distancia recorrida
                    orden_recorrido.append((vecino, nivel + 1, distancia_recorrida))  # Agregar info del vecino al orden de recorrido
    
    # Devolver el orden del recorrido que contiene información sobre el nivel y distancia de cada nodo
    return orden_recorrido

# Nodo inicial y nodos objetivo
nodo_inicial = 'UAI-Las Condes'
objetivo_nodos = {'El Golf', 'Vitacura', 'La Reina', 'Lo Barnechea', 'Ñuñoa', 'La Dehesa', 'Providencia', 'Santiago Centro', 'Independencia', 'Renca', 'San Miguel', 'La Cisterna','Lo Espejo', 'La Granja', 'La Florida'}


orden_recorrido = bfs(grafo, nodo_inicial, objetivo_nodos)

# Imprimir el orden completo del recorrido con el nivel de cada nodo
print("Orden del recorrido con el nivel de cada nodo:")
for nodo, nivel, distancia in orden_recorrido:
    print(f"Nodo: {nodo}, Nivel: {nivel}, Distancia: {distancia}")
