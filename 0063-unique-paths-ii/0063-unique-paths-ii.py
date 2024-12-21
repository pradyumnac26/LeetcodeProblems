class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def f(i, j) : 
            if i==0 and j == 0 : 
                return 1
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1: 
                return 0
            if dp[i][j] != -1 : 
                return dp[i][j]
            up = f(i-1, j)
            left = f(i, j-1)
            dp[i][j] = up + left
            return dp[i][j]


        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1]*m for i in range(n)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1 : 
            return 0

        return f(n-1,m-1)
        