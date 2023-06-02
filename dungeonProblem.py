from collections import deque
from typing import List, Tuple


# find start and end positions
def findPositions(map: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start, end = None, None

    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "S":
                start = (r, c)
            elif map[r][c] == "E":
                end = (r, c)

    return start, end


# find path from start to end
def findPath(
    map: List[List[str]],
    start: Tuple[int, int],
    end: Tuple[int, int],
) -> List[Tuple[int, int]]:
    queue = deque([start])  # queue for bfs
    visited = {start: None}  # dictionary to keep a track of paths
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # [S, N, W, E]

    while queue:
        curr = queue.popleft()
        if curr == end:
            path = []
            while curr is not None:
                path.append(curr)
                curr = visited[curr]

            return path[::-1]

        for r, c in directions:
            new_r, new_c = r + curr[0], c + curr[1]
            new_pos = (new_r, new_c)

            # check first if the new coords are in bounds
            # check if it is not on a road block
            # check if it is not visited earlier
            if (
                0 <= new_r < len(map)
                and 0 <= new_c < len(map[0])
                and map[new_r][new_c] != "#"
                and new_pos not in visited
            ):
                visited[new_pos] = curr
                queue.append(new_pos)

    return None


if __name__ == "__main__":
    map = [
        ["S", ".", ".", "#", ".", ".", "."],
        [".", "#", ".", ".", ".", "#", "E"],
        [".", "#", ".", ".", ".", ".", "."],
        [".", ".", "#", "#", ".", ".", "."],
        ["#", ".", "#", "#", ".", "#", "."],
    ]

    start, end = findPositions(map)
    if start and end:
        path = findPath(map, start, end)
        if path:
            print("->".join([f" ({r},{c}) " for r, c in path]))
        else:
            print("Path not found.")
    else:
        print("Start/end not found.")
