class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        curi = 0
        def dfs(r,c, visited): 
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == 0 or (r,c) in visited: 
                return 0
            visited.add((r,c))
            res = grid[r][c]
            for dr, dc in directions :
                new_row, new_col = r + dr, c + dc
                res = max(res, grid[r][c] + dfs(new_row, new_col, visited))

            return res


        maxi = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] !=0: 
                    maxi = max(maxi, dfs(i, j, set()))
        return maxi
        