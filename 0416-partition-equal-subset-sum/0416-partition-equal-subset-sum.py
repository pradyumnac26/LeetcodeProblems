class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2 !=0 : 
            return False
        total = target // 2 

        dp = [[False]*(total+1) for _ in range(len(nums)+1)] 
        for i in range(len(nums)+1) : 
            dp[i][0] = True 

        if nums[0] <= total:
            dp[1][nums[0]] = True
        
            
        for i in range(1, len(nums)+1) : 
            for s in range(1, total+1) : 
                if s < nums[i-1] : 
                    dp[i][s] = dp[i-1][s] 
                else : 
                    dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i-1]]

        return dp[len(nums)][total]
        