class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        vis =set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(r, c): 
            vis.add((r, c))
            area = 1
            for dr, dc in directions : 
                new_row, new_col = r + dr, c + dc
                if 0<=new_row<ROWS and 0 <=new_col<COLS and (new_row, new_col) not in vis and grid[new_row][new_col] == 1 : 
                    area += dfs(new_row, new_col)
                    
            return area



        maxarea = 0
        for i in range(len(grid)): 
            for j in range(COLS): 
                if grid[i][j] == 1 : 
                    maxarea = max(maxarea, dfs(i, j))
                    
        return maxarea
        


        