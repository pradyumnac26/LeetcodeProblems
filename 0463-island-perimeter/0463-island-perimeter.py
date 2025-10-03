class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        peri = 0 
        vis = set()

        def dfs(r, c) : 
            if r < 0 or r >= rows or c < 0 or c >= cols : 
                return 1
            if grid[r][c] == 0 : 
                return 1
            if (r, c) in vis : 
                return 0
            
            vis.add((r, c))
            peri = dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1) + dfs(r-1, c)
            print(peri)
            
            return peri

        for i in range(rows): 
            for j in range(cols) : 
                if grid[i][j] == 1 : 
                    return dfs(i, j)


        