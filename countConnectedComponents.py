from typing import Dict, Set


def dfs(graph: Dict, node: str, visited: Set, components: Dict, count: int) -> bool:
    stack = [node]
    while len(stack) > 0:
        curr = stack.pop()
        if curr in visited:
            return False
        components[curr] = count + 1
        visited.add(curr)
        for neighbor in graph[curr]:
            dfs(graph, neighbor, visited, components, count)

    return True


def countConnectedComponents(graph: Dict) -> int:
    count = 0
    visited = set()
    components = {}
    for node in graph:
        if node in visited:
            continue
        count += dfs(graph, node, visited, components, count)

    return count, components


if __name__ == "__main__":
    """
                 i
                / \
               j - k
                  / \
                 l   m         n - o
    """

    graph = {
        "i": ["j", "k"],
        "j": ["k", "i"],
        "k": ["i", "j", "l", "m"],
        "l": ["k"],
        "m": ["k"],
        "n": ["o"],
        "o": ["n"],
    }
    visited = set()
    num_comp, components = countConnectedComponents(graph)
    print(f"Number of components: {num_comp}")
    print()

    for k, v in components.items():
        print(f"Node {k} belongs to component {v}")
