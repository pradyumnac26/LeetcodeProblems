class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0 
        flag = True
        for i in range(1, len(nums)): 
            if nums[i] <= nums[i-1] : 
                ans = ans + (nums[i-1] - nums[i]+1)
                nums[i] = nums[i-1]+1
        return ans 

