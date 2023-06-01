from typing import Dict
from collections import deque


def bfs(graph: Dict, start_node: str):
    queue = deque(start_node)
    visited = set()

    while len(queue) > 0:
        curr = queue.popleft()
        if curr in visited:
            continue
        print(curr)
        if curr not in graph:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)


if __name__ == "__main__":
    graph = {
        "i": ["k", "j", "m"],
        "j": ["k", "i"],
        "k": ["i", "j", "l"],
        "l": ["k"],
    }
    bfs(graph, "i")
