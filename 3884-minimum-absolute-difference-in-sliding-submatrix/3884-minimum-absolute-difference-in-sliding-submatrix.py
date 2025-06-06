class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                values = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        values.append(grid[r][c])
                values.sort()
                min_diff = float('inf')
                for d in range(1, len(values)):
                    if values[d] != values[d - 1]:
                        min_diff = min(min_diff, abs(values[d] - values[d - 1]))
                result[i][j] = min_diff if min_diff != float('inf') else 0  # If all elements are same
        return result