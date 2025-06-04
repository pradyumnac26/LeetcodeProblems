from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        # Adjust for start cell's cost
        start_health = health - grid[0][0]
        if start_health < 1:
            return False

        q = deque()
        q.append((0, 0, start_health))
        visited = dict()
        visited[(0, 0)] = start_health

        while q:
            r, c, h = q.popleft()
            

            if r == ROWS - 1 and c == COLS - 1 and h >= 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    new_health = h - grid[nr][nc]
                    if new_health >= 1:
                        if (nr, nc) not in visited or visited[(nr, nc)] < new_health:
                            visited[(nr, nc)] = new_health
                            q.append((nr, nc, new_health))

        return False
