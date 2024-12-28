class Solution:
    def largestDivisibleSubset(self, nums):
        # Edge case: if nums is empty, return an empty list
        if not nums:
            return []

        # Sort the array to ensure that we only check in one direction (nums[i] % nums[j] where i > j)
        nums.sort()

        # dp[i] will store the size of the largest divisible subset that ends with nums[i]
        dp = [1] * len(nums)

        # prev[i] will store the index of the previous element in the subset
        prev = [-1] * len(nums)

        # Fill the dp and prev arrays
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:  # nums[i] can be added to the subset of nums[j]
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # Find the index of the largest subset using built-in functions
        max_size = max(dp)  # Maximum size of the divisible subset
        max_index = dp.index(max_size)  # Index where the largest subset ends

        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        # Reverse the result to get the subset in the correct order
        return result[::-1]

# Example usage:
sol = Solution()
nums1 = [1, 2, 3]
print(sol.largestDivisibleSubset(nums1))  # Output: [1, 2]

nums2 = [1, 2, 4, 8]
print(sol.largestDivisibleSubset(nums2))  # Output: [1, 2, 4, 8]
