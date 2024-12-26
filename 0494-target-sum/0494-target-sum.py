from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums, target):
        # Start the recursion from the last index
        self.nums = nums  # Store nums in the class instance
        self.target = target
        return self.cal(len(nums) - 1, 0)  # Start from the last index and an initial sum of 0

    @lru_cache(None)  # Cache the results of the function calls
    def cal(self, idx, currSum):
        # Base case: If we've processed all elements
        if idx == -1:
            return 1 if currSum == self.target else 0
        
        # Recurse by adding the current number
        add = self.cal(idx - 1, currSum + self.nums[idx])
        
        # Recurse by subtracting the current number
        sub = self.cal(idx - 1, currSum - self.nums[idx])
        
        # Return the total number of valid ways (adding and subtracting the number)
        return add + sub
