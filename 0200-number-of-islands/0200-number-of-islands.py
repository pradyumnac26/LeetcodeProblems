class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c) : 

            if r  < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) : 
                return 
            if grid[r][c] == "0" : 
                return 
            if vis[r][c] == True : 
                return

            vis[r][c] = True

            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)


        islands = 0 
        rows, cols = len(grid), len(grid[0])
        vis = [[False] * cols for _ in range(rows)]

        for i in range(len(grid)) : 
            for j in range(len(grid[0])): 
                if grid[i][j] == "1" and vis[i][j]!=True: 
                    dfs(i, j)
                    islands+=1
        return islands

        