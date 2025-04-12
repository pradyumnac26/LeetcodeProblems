class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # (max_row-min_row)*(max_col - min_col)

        rows = len(grid)
        cols = len(grid[0])
        min_row, max_row = rows, -1
        min_col, max_col = cols, -1
        for r in range(len(grid)) : 
            for c in range(len(grid[0])) : 
                if grid[r][c] == 1 : 
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        if max_row == -1:
            return 0
        return (max_row - min_row + 1)*(max_col - min_col + 1)


        