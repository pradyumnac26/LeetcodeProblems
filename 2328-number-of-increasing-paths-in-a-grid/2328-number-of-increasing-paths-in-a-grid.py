class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        dp = [[-1] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]

            ans = 1  # path containing only this cell

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c]:
                    ans = (ans + dfs(nr, nc)) % MOD

            dp[r][c] = ans
            return dp[r][c]

        total = 0
        for r in range(rows):
            for c in range(cols):
                total = (total + dfs(r, c)) % MOD

        return total