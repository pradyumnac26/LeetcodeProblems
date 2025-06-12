class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxdiff = float('-inf')
        for i in range(1, len(nums)): 
            diff = abs(nums[i] - nums[i-1])
            maxdiff = max(diff, maxdiff)
        return max(maxdiff, abs(nums[-1] - nums[0]))
        