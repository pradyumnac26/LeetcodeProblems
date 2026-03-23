class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float("inf")] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):
                for dj in [-1, 0, 1]:
                    prev_j = j + dj
                    if 0 <= prev_j < n:
                        dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i - 1][prev_j])

        return min(dp[-1])