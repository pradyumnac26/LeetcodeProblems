class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        peri = 0 
        pre = [nums[0]]*len(nums)
        for i in range(1, len(nums)-1): 
            pre[i] = pre[i-1] + nums[i] 
        
            if pre[i] > nums[i+1] : 
                peri = max(pre[i] + nums[i+1], peri)
        print(pre)
        return peri if peri!=0 else -1


        