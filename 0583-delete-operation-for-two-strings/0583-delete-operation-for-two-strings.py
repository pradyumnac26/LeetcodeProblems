class Solution:
    def solve(self, ind1, ind2, word1, word2, dp):
        # Base case: If either index goes out of bounds
        if ind1 < 0 or ind2 < 0:
            return 0

        # If already computed, return the stored value
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # If characters match, add 1 and solve for the next indices
        if word1[ind1] == word2[ind2]:
            dp[ind1][ind2] = 1 + self.solve(ind1 - 1, ind2 - 1, word1, word2, dp)
            return dp[ind1][ind2]

        # If characters don't match, take the maximum by moving one index at a time
        dp[ind1][ind2] = max(
            self.solve(ind1 - 1, ind2, word1, word2, dp), 
            self.solve(ind1, ind2 - 1, word1, word2, dp)
        )
        return dp[ind1][ind2]

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]  # DP table with -1 (uncomputed)
        lcs_length = self.solve(n - 1, m - 1, word1, word2, dp)  # Find LCS length
        return n + m - 2* lcs_length  # Minimum deletions required

 # Output: 4
