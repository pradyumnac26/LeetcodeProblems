from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() 
        vis = set()
        t = 0 
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        fresh = 0 
        
        # collect initial state
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 2: 
                    q.append((i, j))
                    vis.add((i, j))
                if grid[i][j] == 1: 
                    fresh += 1
        
        # BFS level by level
        while q:
            for _ in range(len(q)):    # process one full minute
                x, y = q.popleft()
                for dr, dc in directions:
                    r, c = x+dr, y+dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r,c) not in vis:
                        q.append((r,c))
                        vis.add((r,c))
                        grid[r][c] = 2
                        fresh -= 1
            if q:   # only increment after finishing the full minute
                t += 1
        
        return t if fresh == 0 else -1
