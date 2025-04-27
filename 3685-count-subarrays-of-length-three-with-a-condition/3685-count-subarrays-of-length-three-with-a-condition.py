class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = 0 
        r = 2 
        cnt = 0 
        while r < len(nums): 
            if nums[l] + nums[r] == nums[r-1]/2 : 
                cnt = cnt + 1
            l = l+1
            r = r +1
        return cnt
        