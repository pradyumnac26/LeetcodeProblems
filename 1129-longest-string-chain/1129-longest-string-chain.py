class Solution:
    def is_predecessor(self, s1, s2):
        # Check if s2 is a predecessor of s1
        if len(s1) != len(s2) + 1:
            return False

        first = 0
        second = 0

        while first < len(s1):
            if second < len(s2) and s1[first] == s2[second]:
                first += 1
                second += 1
            else:
                first += 1

        return first == len(s1) and second == len(s2)

    def longestStrChain(self, words):
        n = len(words)

        # Sort the array in ascending order of string length
        words.sort(key=len)

        dp = [1] * n  # Each word can be a chain of at least length 1

        for i in range(n):
            for prev_index in range(i):
                if self.is_predecessor(words[i], words[prev_index]) and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]

        # Use max() function to find the length of the longest chain
        return max(dp)



