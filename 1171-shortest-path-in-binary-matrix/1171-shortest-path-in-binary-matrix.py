from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # \U0001f6ab If start or end are blocked → no path
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # \U0001f501 All 8 possible directions (including diagonals)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        # \U0001f9e0 BFS queue: (row, col, distance)
        q = deque([(0, 0, 1)])
        grid[0][0] = 1  # mark visited
        
        while q:
            r, c, dist = q.popleft()
            
            # \U0001f3af If we reach bottom-right → shortest path found
            if r == n - 1 and c == n - 1:
                return dist
            
            # Explore all 8 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Valid & unvisited & clear cell
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # mark visited
                    q.append((nr, nc, dist + 1))
        
        # ❌ No path found
        return -1

        