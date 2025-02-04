class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1 
        decreasing = 1
        maxi = 1
        for i in range(1, len(nums)) : 
            if nums[i] > nums[i-1] : 
                increasing += 1
            else : 
                increasing= 1 
            if nums[i] < nums[i-1]: 
                decreasing +=1 
            else: 
                decreasing = 1
                

            maxi = max(maxi, increasing, decreasing)
        return maxi

        