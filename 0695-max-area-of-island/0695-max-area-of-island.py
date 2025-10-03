class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # return the maximum area of island in grid, if there is no island,, return 0
        # meaning which island has more number of cells.
        rows, cols = len(grid), len(grid[0])
        vis = [[False]*cols for _ in range(rows)]
        def dfs(r, c, area) : 
            if r < 0 or r >= rows or c < 0 or c >= cols : 
                return area
            if grid[r][c] == 0 : 
                return area
            if vis[r][c] == True : 
                return area
            vis[r][c] = True
            area = area + 1 
            area = dfs(r+1, c, area)
            area = dfs(r, c+1, area)
            area = dfs(r, c-1, area)
            area = dfs(r-1, c, area)
            return area

        area = 0 
        maxarea =0
        for i in range(rows) : 
            for j in range(cols) : 
                if grid[i][j] == 1 and vis[i][j] == False : 
                    maxarea = max(dfs(i, j, 0), maxarea) 
        return maxarea



        