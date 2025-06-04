from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        q = deque()
        q.append((0, 0, 0, k))

        visited = set()
        visited.add((0, 0, k))

        while q:
            r, c, steps, rem_k = q.popleft()


            if r == ROWS - 1 and c == COLS - 1:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    new_k = rem_k - grid[nr][nc]  # subtract 1 if obstacle
                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        visited.add((nr, nc, new_k))
                        q.append((nr, nc, steps + 1, new_k))

        return -1  
