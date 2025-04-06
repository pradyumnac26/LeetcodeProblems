class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n         # dp[i] = length of longest divisible subset ending at i
        prev = [-1] * n      # prev[i] = index of previous element in subset
        max_len = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # Reconstruct subset
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]

        return res[::-1]  # Reverse to get correct order
