class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:


        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        for j in range(m) : 
            dp[n-1][j] = matrix[n-1][j] 

        for i in range(n-2, -1, -1) : 
            for j in range(m) : 
                down, leftdown, rightdown = float('inf'), float('inf'), float('inf')
                down = matrix[i][j] + dp[i+1][j] 
                leftdown = matrix[i][j] + dp[i + 1][j - 1] if j - 1 >= 0 else float('inf')
                rightdown = matrix[i][j] + dp[i + 1][j + 1] if j + 1 < m else float('inf')

                dp[i][j] = min(down, leftdown, rightdown) 
        return min(dp[0])
