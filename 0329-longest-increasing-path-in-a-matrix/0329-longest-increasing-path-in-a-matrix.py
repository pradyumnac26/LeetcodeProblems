class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(r, c) : 
            if dp[r][c] !=-1 : 
                return dp[r][c]
            leng = 1 
            for dr, dc in directions : 
                new_r, new_c = r + dr, c + dc 
                if 0<=new_r<len(matrix) and 0<=new_c < len(matrix[0]) and matrix[new_r][new_c] > matrix[r][c] : 
                    leng = max(leng, 1 + dfs(new_r, new_c))
            dp[r][c] = leng
            return dp[r][c]



        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dp = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        maxi = 0 
        for i in range(len(matrix)): 
            for j in range(len(matrix[0])) : 
                maxi = max(maxi, dfs(i, j))
        return maxi



        