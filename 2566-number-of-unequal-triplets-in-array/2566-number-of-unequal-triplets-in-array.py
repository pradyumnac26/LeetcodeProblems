class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0 
        for i in range(len(nums)): 
            for j in range(i+1, n) : 
                for k in range(j+1, n) : 
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[k]!=nums[i] : 
                        count = count +1
        return count 


        