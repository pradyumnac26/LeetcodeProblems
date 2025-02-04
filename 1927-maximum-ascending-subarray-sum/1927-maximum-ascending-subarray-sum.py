class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sumi = nums[0] 
        r = 1 
        n = len(nums)
        maxSum = nums[0]
        while r < n : 

            while r < n and nums[r] > nums[r-1] : 
                sumi = sumi + nums[r] 
                r = r + 1
            
            maxSum = max(maxSum, sumi)
            if r < n : 
                sumi = nums[r] 
                r = r + 1 
        return maxSum




        