from typing import List, Set


def maxIslandArea(map: List[List[int]]) -> int:
    visited = set()
    maxArea = 0

    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 1 and (r, c) not in visited:
                area = explore(map, r, c, visited)
                maxArea = max(area, maxArea)

    return maxArea


def explore(map: List[List[int]], r: int, c: int, visited: Set) -> int:
    pos = (r, c)

    rowInBounds = 0 <= r < len(map)
    colInBounds = 0 <= c < len(map[0])

    if not rowInBounds or not colInBounds:
        return 0

    if map[r][c] == 0:
        return 0

    if pos in visited:
        return 0
    visited.add(pos)

    area = 1
    area += explore(map, r + 1, c, visited)
    area += explore(map, r - 1, c, visited)
    area += explore(map, r, c + 1, visited)
    area += explore(map, r, c - 1, visited)

    return area


if __name__ == "__main__":
    map = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]

    print(f"Max area among the islands is: {maxIslandArea(map)}")
