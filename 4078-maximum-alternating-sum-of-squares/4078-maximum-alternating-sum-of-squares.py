class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        for i in range(len(nums)) : 
            if nums[i] < 0 : 
                nums[i] = -1*(nums[i])
        
        nums.sort() 
        res = [0]*len(nums)
        i = len(nums)-1 
        j = 0 
        if len(nums) == 1 : 
            return nums[0]**2
        while i > 0 and j < len(nums): 
            res[j] = nums[i] 
            j = j+2 
            i = i -1
        j = 1 
        print(i)
        while j < len(nums) and i >= 0 : 
            res[j] = nums[i] 
            j = j + 2 
            i = i-1 
        print(res)
        sumi = 0 
        for i in range(len(res)) : 
            if i%2 == 0 : 
                sumi = sumi + (res[i])**2 
            else : 
                sumi = sumi - (res[i])**2 
        return sumi

        
        




        

        