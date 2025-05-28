class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = 0 
        directions = [(1, 0), (0,1), (-1, 0), (0,-1)]
        def dfs(r,c, visited): 
            nonlocal path
            if r < 0 or r >=ROWS or c >= COLS or c < 0 or (r,c) in visited or grid[r][c] == -1: 
                return 
            if grid[r][c] == 2 : 
                if len(visited) == cnt + 1 : 
                    path = path + 1
            visited.add((r, c))
            for dr,dc in directions : 
                new_row, new_col = r + dr, c + dc 
                dfs(new_row, new_col, visited)
            visited.remove((r,c))


        cnt = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 1 : 
                    r,c = i,j
                if grid[i][j] == 0: 
                    cnt = cnt + 1 

        dfs(r,c, set())
        return path

        