import random
from copy import deepcopy


def map(n):
    graph = []
    for i in range(n):
        if i == 0:
            graph = [[0] + randomWeights(n - 1)]
        else:
            graph += [randomWeights(i) + [0] + randomWeights(n - i - 1)]
    return graph


def randomWeights(i) -> list:
    return [random.randint(0, 5) for _ in range(i)]


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
    passables = []
    for v in neighborhood(a, graph):
        if v == b:
            passables = addToPassables(passables, [b], a, False)
            continue
        elif graph[v] == [0 for _ in range(len(graph))]:
            continue
        elif graph[v][b] != 0:
            passables = addToPassables(passables, [b], v, isFirst)
            continue
        else:
            copyOfGraph = deepcopy(graph)
            copyOfGraph[a] = [0 for _ in range(len(graph))]
            paths = findAllPaths(v, b, copyOfGraph, False)
            if len(paths) > 0:
                if paths[0].__class__ == list.__class__:  # is paths a 2D list?
                    for path in paths:
                        if len(path) > 0:
                            if path[-1] == graph[b]:
                                passables = addToPassables(passables, path, v, isFirst)
                else:
                    if paths[-1] == b:
                        passables = addToPassables(passables, paths, v, isFirst)
    return passables


def addToPassables(passables, path, v, isFirst):
    print("\n", passables, path)
    if isFirst:
        if len(passables) > 0:
            if type(passables[0]) == type(0):
                passables = [passables] + [[0, v] + path]
            else:
                passables = passables + [[0, v] + path]
        else:
            passables = [0, v] + path
    else:
        if len(passables) > 0:
            if type(passables[0]) == type(0):
                passables = [passables] + [[v] + path]
            else:
                passables = passables + [[v] + path]
        else:
            passables = [v] + path
    print(passables)
    return passables


def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections


graph = map(10)
for line in graph:
    print(f"{line},")

a = 0
b = 5
c = 9
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
