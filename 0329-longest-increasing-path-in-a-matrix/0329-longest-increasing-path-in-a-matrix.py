class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1,0), (0,-1)] 


        def dfs(r, c) : 
            if dp[r][c] !=-1 : 
                return dp[r][c]

            leng = 1
            for dr, dc in directions : 
                new_r = r + dr 
                new_c = c + dc 
                if new_r < ROWS and new_r >= 0 and new_c < COLS and new_c >= 0 : 
                    if matrix[new_r][new_c] > matrix[r][c] : 
                        leng = max( leng, 1+dfs(new_r, new_c))
            dp[r][c] = leng
            return dp[r][c]



        ROWS = len(matrix) 
        COLS = len(matrix[0])
        res = 0
        dp = [[-1]*COLS for _ in range(ROWS)]

        for i in range(len(matrix)): 
            for j in range(len(matrix[0])): 
                res = max(res, dfs(i, j))
        return res

        