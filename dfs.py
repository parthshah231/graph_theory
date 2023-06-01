from typing import Dict, Set


def printDepthFirst(graph: Dict, start_node: str, visited: Set):
    if start_node in visited:
        return
    visited.add(start_node)
    print(start_node)

    for neighbor in graph[start_node]:
        printDepthFirst(graph, neighbor, visited)


if __name__ == "__main__":
    graph = {
        "i": ["j", "k"],
        "j": ["k", "i"],
        "k": ["i", "j", "l", "m"],
        "l": ["k"],
        "m": ["k"],
    }
    visited = set()
    printDepthFirst(graph, "i", visited)
