class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def f(i,j) : 
            if i == 0 : 
                return matrix[0][j] 
            if j < 0 or j >= m : 
                return float('inf')
            if dp[i][j] != -1 : 
                return dp[i][j] 
            up = matrix[i][j] + f(i-1,j)
            ld = matrix[i][j] + (f(i - 1, j - 1) if j - 1 >= 0 else float('inf'))
            rd = matrix[i][j] + (f(i - 1, j + 1) if j + 1 < m else float('inf'))
            dp[i][j] = min(up,ld,rd) 
            return dp[i][j]

            


        n = len(matrix)
        m = len(matrix[0])
        mini = float('inf')
        dp = [[-1]*m for i in range (n)]
        for j in range(m) : 
           mini = min(mini, f(n-1,j))
        return mini
        
        