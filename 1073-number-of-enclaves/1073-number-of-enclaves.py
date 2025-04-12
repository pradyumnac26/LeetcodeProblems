class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # we can do dfs or bfs here we are just traversiving starting from the boundaries
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c) : 
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 : 
                return 
            grid[r][c] = 0 
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dr,dc in directions : 
                dfs(r+dr, c+dc)


        for r in range(rows) : 
            for c in range(cols): 
                if (r== 0 or c==0 or r == rows-1 or c == cols-1) and grid[r][c] == 1 :
                    dfs(r,c)

        count = 0 
        for i in range(rows) : 
            for j in range(cols) : 
                if grid[i][j] == 1 : 
                    count = count + 1
        return count 







        