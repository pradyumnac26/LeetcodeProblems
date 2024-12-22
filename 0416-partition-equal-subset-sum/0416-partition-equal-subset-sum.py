class Solution:
    def canPartition(self, nums: List[int]) -> bool:
   
        def f(i, target) : 
            if target == 0 : 
                return True 
            if i == 0 : 
                return nums[0] == target 
            if dp[i][target] != -1 : 
                return dp[i][target]

            nottaken = f(i - 1, target)
            taken = False
            if target >= nums[i] : 
                taken = f(i -1, target - nums[i])
            dp[i][target] = taken or nottaken
            return dp[i][target]

        totalSum = sum(nums)
        k = totalSum//2 
        if totalSum % 2 == 1 : 
            return False
        else : 
            dp = [[-1]*(k+1) for i in range(len(nums))]
            return f(len(nums)-1, k)

        