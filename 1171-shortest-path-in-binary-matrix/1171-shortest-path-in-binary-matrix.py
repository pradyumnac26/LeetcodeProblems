class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1 : 
            return -1
        q = deque([])
        q.append((0, 0, 1))
        grid[0][0] = 1 
        while q :
            r, c, steps = q.popleft()
            if r == ROWS - 1 and c == COLS -1 : 
                return steps

            for dr, dc in directions : 
                new_row, new_col = r + dr, c + dc
                if 0<=new_row<ROWS and 0<=new_col<COLS and grid[new_row][new_col] == 0 : 
                    q.append((new_row, new_col, steps + 1))
                    grid[new_row][new_col] = 1

        return -1