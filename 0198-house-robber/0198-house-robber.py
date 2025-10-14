class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(i): 
            if i < 0 : 
                return 0 
            if i == 0 : 
                return nums[0]
            if dp[i] != -1 : 
                return dp[i]
            
            pick = nums[i] + f(i-2)
            nopick = f(i-1)
            dp[i] = max(pick, nopick)
            return dp[i]


        dp = [-1]*len(nums)
        return f(len(nums)-1) 
        