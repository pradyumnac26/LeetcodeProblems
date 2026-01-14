class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        cnt = 0 
        for i in range(len(nums)): 
            s = set() 
            sub_sum = 0 
            for j in range(i, len(nums)): 
                sub_sum += nums[j] 
                s.add(nums[j]) 
                if sub_sum in s : 
                    cnt+=1 
        return cnt  




        