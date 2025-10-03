class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c) : 
            if r < 0 or r >= rows or c < 0 or c >= cols : 
                return False 
            if (r, c) in vis : 
                return True
            if grid[r][c] == 1 : 
                return True
            vis.add((r, c))
            down  = dfs(r+1, c)
            up    = dfs(r-1, c)
            right = dfs(r, c+1)
            left  = dfs(r, c-1)

    # island is closed only if ALL sides are closed
            return down and up and right and left
            
        x = 0
        vis = set()
        for i in range(rows): 
            for j in range(cols) : 
                if grid[i][j] == 0 and (i, j) not in vis : 
                    if dfs(i, j) : 
                        x = x +1 
        return x

        

        