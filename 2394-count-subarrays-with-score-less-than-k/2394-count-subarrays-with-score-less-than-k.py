class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0 
        count = 0 
        sumi = 0 
        for r in range(len(nums)): 
            sumi = sumi + nums[r] 
            score = sumi*(r-l+1)

            while score >= k : 
                sumi = sumi - nums[l] 
                l = l+1
                score = sumi*(r-l+1)
            

            count = count + (r-l+1)
        return count

        