class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # nums = [2, 1, 2]
        nums.sort()
        maxperi = 0 
        for i in range(len(nums)-2): 
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if a + b > c : 
                maxperi = max(maxperi, a+b+c) 
        return maxperi if maxperi!=0 else 0 

        