class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums) 
        cnt = [1]*len(nums)

        for i in range(len(nums)-1, -1, -1) : 
            for j in range(i+1, len(nums)) : 
                if nums[i] < nums[j] : 
                    if 1 + dp[j] > dp[i] : 
                        dp[i] = 1 + dp[j] 
                        cnt[i] = cnt[j]
                    elif 1 + dp[j] == dp[i] : 
                        cnt[i] += cnt[j] 
        L = max(dp) 
        ans = 0 
        for i in range(len(dp)) : 
            if dp[i] == L : 
                ans+= cnt[i] 
        return ans




        