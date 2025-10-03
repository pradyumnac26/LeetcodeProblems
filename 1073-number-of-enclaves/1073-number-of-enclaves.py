class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(r, c) : 
            if r < 0 or r >= rows or c < 0 or c >= cols : 
                return 
            if grid[r][c] == 0 : 
                return
            grid[r][c] = 0
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c) 
            dfs(r, c-1)

        rows, cols = len(grid), len(grid[0])
        for i in range(rows) : 
            for j in range(cols) : 
                if i == 0 or j  == 0 or i == rows-1 or j == cols - 1 :
                    if grid[i][j] == 1 : 
                        dfs(i, j)
                    
        cnt = 0
        for i in range(rows) : 
            for j in range(cols) : 
                if grid[i][j] == 1 : 
                    cnt +=1 
        return cnt






        