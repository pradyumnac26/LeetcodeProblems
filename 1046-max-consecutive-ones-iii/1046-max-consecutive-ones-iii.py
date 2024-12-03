class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0 
        maxLen = 0 
        l = 0
        r = 0 
        while r < len(nums) :
            if nums[r] == 0 : 
                zeros +=1 
            while zeros > k : 
                if nums[l] == 0 : 
                    zeros -= 1 
                l = l +1
            
            if zeros <=k : 

                maxLen = max(r-l+1, maxLen)
            r=r+1
        return maxLen
                
        