class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 
        if n == 0 : 
            return 0 
        if n == 1 : 
            return nums[0]
        if n == 2 : 
            return max(nums[0], nums[1])

        def f(i, nums, dp): 
            if i < 0 : 
                return 0 
            if i == 0 : 
                return nums[0] 
            if dp[i]!=-1 : 
                return dp[i]

            p = nums[i] + f(i-2, nums, dp)
            np = f(i-1, nums, dp)
            dp[i] = max(p, np)
            return dp[i]
        dp1 = [-1]*(n+1) 
        dp2 = [-1]*(n+1)
        return max(f(n-2, nums[1:], dp1), f(n-2, nums[:-1], dp2))

        
        