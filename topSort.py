from typing import List, Dict, Set


def dfsTopSort(
    graph: Dict[str, List[str]],
    node: str,
    visited: Set[str],
    visitedNodes: List[str],
):
    if node in visited:
        return
    visited.add(node)
    visitedNodes.append(node)
    for neighbor in graph[node]:
        dfsTopSort(graph, neighbor, visited, visitedNodes)


def topSort(graph: Dict[str, List[str]]):
    visited = set()
    ordering = [0 for i in range(len(graph))]
    idx = len(graph) - 1

    for node in graph:
        visitedNodes = []
        if node in visited:
            continue
        dfsTopSort(graph, node, visited, visitedNodes)
        for nodeId in visitedNodes[::-1]:
            ordering[idx] = nodeId
            idx -= 1

    return ordering


if __name__ == "__main__":
    graph = {
        "A": ["D"],
        "B": ["D"],
        "C": ["A", "B"],
        "D": ["H", "G"],
        "E": ["A", "D", "F"],
        "F": ["K", "J"],
        "G": ["I"],
        "H": ["I", "J"],
        "I": ["L"],
        "J": ["L", "M"],
        "K": ["J"],
        "L": [],
        "M": [],
    }

    print(topSort(graph))
