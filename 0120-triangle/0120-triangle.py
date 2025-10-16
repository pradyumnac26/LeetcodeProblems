class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for _ in range(len(triangle[i]))] for i in range(n)]

        # base case: bottom row = same as triangle
        for j in range(len(triangle[n - 1])):
            dp[n - 1][j] = triangle[n - 1][j]

        # build the DP table from bottom-1 row to top
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                down = triangle[i][j] + dp[i + 1][j]
                diagonal = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(down, diagonal)

        # answer at the top
        return dp[0][0]
