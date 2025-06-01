class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        length = 0 
        dp = [[-1]*COLS for _ in range(ROWS)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, c): 
            if dp[r][c] !=-1: 
                return dp[r][c]

            leng = 1
            for dr, dc in directions : 
                new_row, new_col = r+dr, c+dc
                if 0<=new_row<ROWS and 0<=new_col<COLS and matrix[r][c] < matrix[new_row][new_col]:
                    leng = max(leng, 1 + dfs(new_row, new_col)) 
            dp[r][c] = leng
            return dp[r][c]

                
              
        for i in range(ROWS): 
            for j in range(COLS): 
                length = max(length, dfs(i, j) )
        return length 
        