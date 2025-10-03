class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        vis = set() 
        rows, cols = len(grid), len(grid[0])
        total = 0

        def dfs(r, c, total) : 
            if r < 0 or r >= rows or c < 0 or c >= cols : 
                return total 
            if (r, c) in vis : 
                return total 
            if grid[r][c] == 0 : 
                return total
            
            vis.add((r, c))
            total = total + grid[r][c]
            total = dfs(r+1, c, total)
            total = dfs(r-1, c, total)
            total = dfs(r, c-1, total)
            total = dfs(r, c+1, total)
            return total


        maxi = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] > 0 and (i, j) not in vis : 
                    maxi = max(maxi,dfs(i, j, total) )
        return maxi

        