import random
from copy import deepcopy
import time


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


def allPaths(a, b, graph):
    subsets = []
    for n in range(len(graph)):
        copyOfSubsets = deepcopy(subsets)
        n = len(graph) - n - 1
        for set in copyOfSubsets:
            subsets.append([n] + set)
        subsets.append([n])
    copyOfSubsets = deepcopy(subsets)
    for set in subsets:
        if set[0] == a and set[-1] == b:
            for i in range(len(set[:-1])):
                if graph[set[i]][set[i + 1]] == 0:
                    copyOfSubsets.remove(set)
                    break
            continue
        copyOfSubsets.remove(set)
    return copyOfSubsets


def shortestPath(a, b, graph):
    shortestPath = []
    costOfShortestPath = float("inf")
    for path in allPaths(a, b, graph):
        cost = 0
        for i in range(len(path[:-1])):
            cost += graph[path[i]][path[i + 1]]
        if cost < costOfShortestPath:
            shortestPath = path
            costOfShortestPath = cost
        if cost == costOfShortestPath and len(path) < len(shortestPath):
            shortestPath = path
            costOfShortestPath = cost
    return shortestPath


def test(n):
    deltaTimes = []
    for i in range(4):
        start = time.time()
        graph = map(n)

        a = 0
        b = len(graph) - 1

        print(f"shortest path from {a} to {b}: {shortestPath(a, b, graph)}")
        end = time.time()
        deltaTimes += [end - start]
    average = sum(deltaTimes) / len(deltaTimes)
    return f"\n{n}: {round(average, 3)}"


print(f"Times:{test(14)}{test(15)}{test(16)}{test(17)}")


# * Old Code (this solution didn't work very well)

# def allPaths(a, b, graph):
#     return findAllPaths(a, b, graph, True, a)


# def findAllPaths(a, b, graph, isFirst, start):
#     passables = []
#     if a == b:
#         return []
#     for v in neighborhood(a, graph):
#         if graph[v] == [0 for _ in range(len(graph))]:
#             continue
#         if v == b:
#             passables = addToPassables(passables, [b], a, False, start)
#         if graph[v][b] != 0:
#             passables = addToPassables(passables, [b], v, isFirst, start)
#         copyOfGraph = deepcopy(graph)
#         copyOfGraph[a] = [0 for _ in range(len(graph))]
#         paths = findAllPaths(v, b, copyOfGraph, False, start)
#         if len(paths) > 0:
#             if type(paths[0]) != type(0):  # is paths a 2D list?
#                 for path in paths:
#                     if len(path) > 0:
#                         if path[-1] == graph[b]:
#                             passables = addToPassables(
#                                 passables, path, v, isFirst, start
#                             )
#             else:
#                 if paths[-1] == b:
#                     passables = addToPassables(passables, paths, v, isFirst, start)
#     return passables


# def addToPassables(passables, path, v, isFirst, start):
#     # print("\n", passables, [v] + path, isFirst)
#     if path[0] == v:
#         return passables
#     if isFirst:
#         if len(passables) > 0:
#             if type(passables[0]) == type(0):
#                 passables = [passables] + [[start, v] + path]
#             else:
#                 passables = passables + [[start, v] + path]
#         else:
#             passables = [start, v] + path
#     else:
#         if len(passables) > 0:
#             if type(passables[0]) == type(0):
#                 passables = [passables] + [[v] + path]
#             else:
#                 passables = passables + [[v] + path]
#         else:
#             passables = [v] + path
#     # print(passables)
#     return passables

# def neighborhood(vertex, graph):
#     edges = graph[vertex]
#     connections = []
#     for i in range(len(edges)):
#         edge = edges[i]
#         if edge != 0:
#             connections.append(i)
#     return connections
