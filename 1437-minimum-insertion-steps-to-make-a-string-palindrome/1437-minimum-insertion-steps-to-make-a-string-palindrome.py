class Solution:
    def solve(self, ind1, ind2, s, rev, dp):
        # Base case: If either index goes out of bounds
        if ind1 < 0 or ind2 < 0:
            return 0
        
        # If already computed, return the stored value
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
        
        # If characters match, add 1 and solve for the next indices
        if s[ind1] == rev[ind2]:
            dp[ind1][ind2] = 1 + self.solve(ind1 - 1, ind2 - 1, s, rev, dp)
            return dp[ind1][ind2]
        
        # If characters don't match, take the maximum by moving one index at a time
        dp[ind1][ind2] = max(
            self.solve(ind1 - 1, ind2, s, rev, dp), 
            self.solve(ind1, ind2 - 1, s, rev, dp)
        )
        return dp[ind1][ind2]
    
    def minInsertions(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]  # Reverse the string
        dp = [[-1 for _ in range(n)] for _ in range(n)]  # DP table with -1 (uncomputed)
        lcs_length = self.solve(n - 1, n - 1, s, rev, dp)  # Find LCS length
        return n - lcs_length  # Minimum insertions required


