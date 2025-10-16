class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def f(i, j) : 
            if i < 0 or j < 0 : 
                return float('inf') 
            if i == 0 and j == 0 : 
                return grid[0][0]
            if dp[i][j] != -1 : 
                return dp[i][j]
            mini = float('inf')

            up = grid[i][j] + f(i-1, j)
            left = grid[i][j] + f(i, j-1)
            dp[i][j] = min(up, left)
            return dp[i][j]

        dp = [[-1]*len(grid[0]) for _ in range(len(grid))]
        return f(len(grid)-1, len(grid[0])-1)