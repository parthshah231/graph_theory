from typing import List, Set


def countIslands(map: List[List[int]]) -> int:
    visited = set()
    count = 0

    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 1 and (r, c) not in visited:
                count += explore(map, r, c, visited)

    return count


def explore(map: List[List[int]], r: int, c: int, visited: Set) -> bool:
    pos = (r, c)

    rowInBounds = 0 <= r < len(map)
    colInBounds = 0 <= c < len(map[0])

    if not rowInBounds or not colInBounds:
        return False

    if map[r][c] == 0:
        return False

    if pos in visited:
        return False
    visited.add(pos)

    explore(map, r + 1, c, visited)
    explore(map, r - 1, c, visited)
    explore(map, r, c + 1, visited)
    explore(map, r, c - 1, visited)

    return True


if __name__ == "__main__":
    map = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print(f"Number of islands is: {countIslands(map)}")
