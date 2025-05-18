class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumofDigits(n):
            sumi = 0 
            while n > 0: 
                sumi = sumi + n%10
                n = n//10
            return sumi


        for i in range(len(nums)): 
            if i == sumofDigits(nums[i]) : 
                return i 

        return -1

        