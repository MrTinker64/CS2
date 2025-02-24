import random

def map(n):
    graph = []
    for i in range(n):
        if i == 0:
            graph = [[0] + randomWeights(n-1)]
        else:
            graph += [randomWeights(i) + [0] + randomWeights(n-i-1)]
    return graph

def randomWeights(i) -> list:
    return [random.randint(0, 5) for _ in range(i)]

def isPath(a, b, graph):
    if graph[a][b] != 0:
        return True
    else:
        for v in neighborhood(a, graph):
            if graph[v][b] != 0:
                return True
    return False

def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections