class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(n): 
            for j in range(m): 
                if i == 0 and j == 0 and obstacleGrid[i][j] == 0  : 
                    dp[i][j] = 1 
                    continue 
                if obstacleGrid[i][j] == 1 : 
                    dp[i][j] = 0 
                    continue 
                up = 0 
                left = 0 
                if i > 0 : 
                    up = dp[i-1][j] 
                if j > 0 : 
                    left = dp[i][j-1]
                dp[i][j] = up + left
        return dp[n-1][m-1]

        