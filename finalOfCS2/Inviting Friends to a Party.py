import random
from copy import deepcopy


def friends(n):
    graph = []
    for i in range(n):
        if i == 0:
            graph = [[0] + randomWeights(n - 1)]
        else:
            graph += [randomWeights(i) + [0] + randomWeights(n - i - 1)]
    return graph


def randomWeights(i) -> list:
    return [random.randint(0, 1) for _ in range(i)]


def isClique(cq, graph):
    for vertex in cq:
        neighbors = neighborhood(vertex, graph)
        for v in cq:
            if neighbors.count(v) < 1 and v != vertex:
                return False
    return True


def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections


def findCombinations(graph):
    subsets = []
    for n in range(len(graph)):
        copyOfSubsets = deepcopy(subsets)
        print(n)
        n = len(graph) - n - 1
        print(n)
        for set in copyOfSubsets:
            print(set)
            subsets.append([n] + set)
        subsets.append([n])
    return subsets


def largestCliqueIn(graph):
    longestSet = []
    longestLen = float("inf")
    for set in findCombinations(graph):
        if isClique(set, graph) and len(set) < longestLen:
            longestSet = set
            longestLen = len(set)
    return longestSet

# cq = [0, 1, 2]

# print(f"Is {cq} clique: {isClique(cq, graph)}")

print(findCombinations([i for i in range(4)]))
