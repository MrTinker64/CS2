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
                copyOfGraph.pop(a)
                return isPath(v, b, copyOfGraph)
    return False

def checkNeighborsForConnection(a, b, graph):
    print("\n")
    print(a, b)
    print(graph)
    if graph[a][b] != 0:
        return [a, b]
    else:
        for v in neighborhood(a, graph):
            if graph[v][b] != 0:
                return [v, b]
            elif graph[v] == [0 for _ in range(len(graph))]:
                continue
            else:
                copyOfGraph = deepcopy(graph)
                copyOfGraph[a] = [0 for _ in range(len(graph))]
                paths = checkNeighborsForConnection(v, b, copyOfGraph)
                passables = []
                for path in paths:
                    if len(path) > 0:
                        if path[-1] == graph[b]:
                            passables.append[[v] + path]
                return passables
    return []
                

def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections

# def allPaths(a, b, graph):
#     if not isPath(a, b, graph):
#         return []
#     if graph[a][b] != 0:
#         return [a, b]
#     for vertex in len(graph):
#         for neighbor in neighborhood(vertex, graph):

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
print(f"Path from {a} to {b}: {checkNeighborsForConnection(a, b, graph)}")