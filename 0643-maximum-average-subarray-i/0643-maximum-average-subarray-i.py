class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = windowsum = sum(nums[:k])
        l = 0 
        r = k
        while r < len(nums) : 
            windowsum = windowsum + nums[r] - nums[l]
            maxsum = max(maxsum, windowsum)
            l = l+1
            r = r+1
        return maxsum/k
        