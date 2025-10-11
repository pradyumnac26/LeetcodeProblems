class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # subarray problems. 
        # 


        def is_fibonacci(i) : 
            if nums[i-2] + nums[i-1] == nums[i] : 
                return True 
            else : 
                return False

        
        cnt = 1
        longest = 0
        for i in range(len(nums)) : 
            if i >=2 and is_fibonacci(i) : 
                cnt +=1 
            else : 
                cnt = 1 
            longest = max(longest, cnt+1)
        return longest


