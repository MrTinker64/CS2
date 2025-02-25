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
    return len(allPaths(a, b, graph)) > 0
    # TODO need to make this return a list like how allPaths does
    # if graph[a][b] != 0:
    #     return True
    # else:
    #     for v in neighborhood(a, graph):
    #         if graph[v][b] != 0:
    #             return True
    #         elif graph[v] == [0 for _ in range(len(graph))]:
    #             continue
    #         else:
    #             copyOfGraph = deepcopy(graph)
    #             copyOfGraph[a] = [0 for _ in range(len(graph))]
    #             return isPath(v, b, copyOfGraph)
    # return False

def allPaths(a, b, graph):
    return findAllPaths(a, b, graph, True)

def findAllPaths(a, b, graph, isFirst):
    if graph[a][b] != 0:
        return [a, b]
    else:
        passables = []
        for v in neighborhood(a, graph):
            if graph[v][b] != 0:
                if isFirst:
                    return [0, v, b]
                else:
                    return [v, b]
            elif graph[v] == [0 for _ in range(len(graph))]:
                continue
            else:
                copyOfGraph = deepcopy(graph)
                copyOfGraph[a] = [0 for _ in range(len(graph))]
                paths = findAllPaths(v, b, copyOfGraph, False)
                if len(paths) > 0:
                    if paths[0].__class__ == list.__class__: # is paths a 2D list?
                        for path in paths:
                            if len(path) > 0:
                                if path[-1] == graph[b]:
                                    if isFirst:
                                        passables.append([0, v] + path)
                                    else:
                                        passables.append([v] + path)
                    else:
                        if paths[-1] == b:
                            if isFirst:
                                if len(passables) > 0:
                                    passables = [passables] + [[0, v] + paths]
                                else:
                                    passables = [0, v] + paths
                            else:
                                if len(passables) > 0:
                                    passables = [passables] + [[v] + paths]
                                else:
                                    passables = [v] + paths
        return passables                

def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections

graph =  [[0, 1, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 1, 1],
[1, 1, 0, 0, 1, 0],
[0, 1, 1, 1, 0, 0],
[0, 1, 0, 1, 1, 0],]
for line in graph:
    print(f"{line},")

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

print(f"Path from {a} to {b}: {allPaths(a, b, graph)}")
print(f"Path from {a} to {c}: {allPaths(a, c, graph)}")