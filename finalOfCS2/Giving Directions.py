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
    return findAllPaths(a, b, graph, True, a)


def findAllPaths(a, b, graph, isFirst, start):
    passables = []
    if a == b:
        return []
    for v in neighborhood(a, graph):
        if graph[v] == [0 for _ in range(len(graph))]:
            continue
        if v == b:
            passables = addToPassables(passables, [b], a, False, start)
        if graph[v][b] != 0:
            passables = addToPassables(passables, [b], v, isFirst, start)
        copyOfGraph = deepcopy(graph)
        copyOfGraph[a] = [0 for _ in range(len(graph))]
        paths = findAllPaths(v, b, copyOfGraph, False, start)
        if len(paths) > 0:
            if type(paths[0]) != type(0):  # is paths a 2D list?
                for path in paths:
                    if len(path) > 0:
                        if path[-1] == graph[b]:
                            passables = addToPassables(
                                passables, path, v, isFirst, start
                            )
            else:
                if paths[-1] == b:
                    passables = addToPassables(passables, paths, v, isFirst, start)
    return passables


def addToPassables(passables, path, v, isFirst, start):
    # print("\n", passables, [v] + path, isFirst)
    if path[0] == v:
        return passables
    if isFirst:
        if len(passables) > 0:
            if type(passables[0]) == type(0):
                passables = [passables] + [[start, v] + path]
            else:
                passables = passables + [[start, v] + path]
        else:
            passables = [start, v] + path
    else:
        if len(passables) > 0:
            if type(passables[0]) == type(0):
                passables = [passables] + [[v] + path]
            else:
                passables = passables + [[v] + path]
        else:
            passables = [v] + path
    # print(passables)
    return passables


def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections


def shortestPath(a, b, graph):
    shortestPath = []
    costOfShortestPath = float("inf")
    for path in allPaths(a, b, graph):
        cost = 0
        for v in path[:-1]:
            cost += graph[v][v + 1]
        if cost < costOfShortestPath:
            shortestPath = path
            costOfShortestPath = cost
    return shortestPath


graph = [
    [0, 0, 4, 1],
    [5, 0, 3, 4],
    [2, 4, 0, 1],
    [4, 0, 4, 0],
]
for line in graph:
    print(f"{line},")

a = 0
b = 3

print(f"Paths from {a} to {b}: {allPaths(a, b, graph)}")
print(f"Shortest path from {a} to {b}: {shortestPath(a, b, graph)}")
