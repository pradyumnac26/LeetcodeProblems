class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        cnt = 0 
        for k in range(2, n): 
            i = 0 
            j = k -1 
            while i < j : 
                if nums[i] + nums[j] > nums[k] : 
                    cnt+=(j-i)
                    j = j -1 
                else : 
                    i = i + 1 
        return cnt 







        