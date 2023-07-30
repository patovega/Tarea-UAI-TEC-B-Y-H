def dfs(grafo, inicio):
    # Crear un conjunto para almacenar los nodos visitados
    visitados = set()

    # Crear una pila para realizar el recorrido DFS, inicializando con el nodo de inicio y su nivel (0)
    stack = [(inicio, 0)]

    # Variable para llevar un conteo de los pasos realizados durante el recorrido
    paso = 1

    # Variable para almacenar la distancia recorrida durante el DFS
    distancia_recorrida = 0

    # Inicio del ciclo while, que se ejecutará mientras la pila tenga elementos (nodos pendientes de visitar)
    while stack:
        # Extraer el nodo actual y su nivel desde la cima de la pila
        nodo_actual, nivel = stack.pop()

        # Verificar si el nodo actual no ha sido visitado aún
        if nodo_actual not in visitados:
            # Si el nodo no ha sido visitado, agregarlo al conjunto de nodos visitados
            visitados.add(nodo_actual)

            # Imprimir información del paso actual: número de paso, nodo y nivel en el que se encuentra, y distancia recorrida
            print(f"Paso {paso}: Nodo: {nodo_actual}, Nivel: {nivel}, Distancia Recorrida: {distancia_recorrida}")

            # Iterar sobre los vecinos del nodo actual en el grafo
            for vecino in grafo[nodo_actual]:
                # Verificar si el vecino no ha sido visitado aún
                if vecino not in visitados:
                    # Si el vecino no ha sido visitado, agregarlo a la pila con el nivel incrementado en 1
                    stack.append((vecino, nivel + 1))
                    # Incrementar la distancia recorrida en 1 al avanzar al vecino
                    distancia_recorrida += 1

            # Incrementar el contador de pasos para el siguiente ciclo
            paso += 1


# Grafo representado como un diccionario de listas de adyacencia
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
    'La Cisterna': ['San Miguel', 'La Granja', 'Lo Espejo'],
    'La Granja': ['La Cisterna', 'La Florida'],
    'La Florida': ['La Granja'],
    'Lo Espejo': ['La Cisterna', 'San Miguel'],
}

# Nodo de inicio para el recorrido DFS
inicio_dfs = 'UAI-Las Condes'

# Llamada al algoritmo DFS
print("Recorrido DFS:")
dfs(grafo, inicio_dfs)