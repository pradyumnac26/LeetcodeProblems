class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        # Initialize the DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Start from the bottom-right corner of the DP table to construct the answer
        i, j = n, m
        ans = []

        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                ans.append(s[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                ans.append(s[i - 1])
                i -= 1
            else:
                ans.append(t[j - 1])
                j -= 1

        # Add remaining characters from s and t
        while i > 0:
            ans.append(s[i - 1])
            i -= 1
        while j > 0:
            ans.append(t[j - 1])
            j -= 1

        # Reverse the constructed supersequence since we built it backwards
        ans.reverse()
        return ''.join(ans)


