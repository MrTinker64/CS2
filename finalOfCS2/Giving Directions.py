import random
from copy import deepcopy

def map(n):
    graph = []
    for i in range(n):
        if i == 0:
            graph = [[0] + randomWeights(n-1)]
        else:
            graph += [randomWeights(i) + [0] + randomWeights(n-i-1)]
    return graph

def randomWeights(i) -> list:
    return [random.randint(0, 1) for _ in range(i)]

def isPath(a, b, graph):
    if graph[a][b] != 0:
        return True
    else:
        for v in neighborhood(a, graph):
            if graph[v][b] != 0:
                return True
            else:
                copyOfGraph = deepcopy(graph)
                copyOfGraph.remove
                return isPath(v, b, graph)
    return False

def subIsPath(vertex, b, graph, a):
    if graph[vertex][b] != 0:
        return True
    else:
        for v in neighborhood(vertex, graph):
            if graph[vertex][b] != 0 and not v == a:
                return True
            else:
                return subIsPath(vertex, b, graph, a)
    return False

def checkNeighborsForConnection(a, b, graph):
    if graph[a][b] != 0:
        return [a, b]
    else:
        for v in neighborhood(a, graph):
            if graph[v][b] != 0:
                return [a, b]
            else:
                [a] + checkNeighborsForConnection(v, b, graph)
    return []

def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections

def allPaths(a, b, graph):
    if not isPath(a, b, graph):
        return []

graph =  [[0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[1, 0, 0, 1, 1, 0],
[1, 1, 1, 0, 1, 0],
[0, 0, 1, 1, 0, 1],
[1, 1, 1, 0, 1, 0]]
for line in graph:
    print(line)
a = 0
b = 5
c = 3
if isPath(a, b, graph):
    string = "a PATH"
else:
    string = "NOT a path"
if isPath(a, c, graph):
    string2 = "a PATH"
else:
    string2 = "NOT a path"
print(f"{a} to {b} is {string}\n{a} to {c} is {string2}")