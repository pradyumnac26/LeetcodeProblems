class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        currmax = currmin = 0 
        total = 0 
        for n in nums : 
            currmax = max(n + currmax, n)
            currmin = min(n+currmin, n)
            total = total + n
            globalMax = max(globalMax, currmax)
            globalMin = min(globalMin, currmin)
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
        