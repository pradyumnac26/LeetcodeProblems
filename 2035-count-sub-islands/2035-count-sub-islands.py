from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c, grid):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            dfs(r+1, c, grid)
            dfs(r-1, c, grid)
            dfs(r, c+1, grid)
            dfs(r, c-1, grid)

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j, grid2)   # sink this island

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i, j, grid2)
                    count += 1
        return count
