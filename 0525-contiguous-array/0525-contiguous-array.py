class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # hmap to store the difference of ones - zeroes , with the index where it ends . 
        ones = 0 
        zeros = 0 
        hmap = {}
        res = 0
        for i, val in enumerate(nums): 
            if nums[i] == 0: 
                zeros +=1
            else : 
                ones +=1 
            
            diff = ones - zeros

            if diff not in hmap : 
                hmap[diff] = i 

            if ones == zeros : 
                res = ones + zeros
            else : 
                res = max(res, i - hmap[ones-zeros])
            
        return res




