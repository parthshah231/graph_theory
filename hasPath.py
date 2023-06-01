from typing import Dict
from collections import deque


def hasPath(graph: Dict, start_node: str, destn: str) -> bool:
    queue = deque(start_node)
    visited = set()

    while len(queue) > 0:
        curr = queue.popleft()
        if curr == destn:
            return True
        if curr in visited:
            continue
        if curr not in graph:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)

    return False


if __name__ == "__main__":
    graph = {
        "i": ["j", "k"],
        "j": ["k", "i"],
        "k": ["i", "j", "l", "m"],
        "l": ["k"],
        "m": ["k"],
    }
    print(hasPath(graph, "i", "m"))
