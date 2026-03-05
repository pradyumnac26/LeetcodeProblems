class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0 
        l = 0 
        prod = 1 
        if k<=1 : 
            return 0
        for r in range(len(nums)): 
            prod = prod * nums[r] 
            while prod >= k : 
                prod = prod // nums[l] 
                l = l + 1


            count = count + (r-l+1)
        return count
        