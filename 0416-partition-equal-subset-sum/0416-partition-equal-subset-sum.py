class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def f(i, sumi, target) :
            if sumi == target : 
                return True 
            if i >= len(nums) or sumi > target : 
                return False
            if dp[i][sumi] != -1 : 
                return dp[i][sumi]

            dp[i][sumi] = f(i+1, sumi + nums[i], target) or f(i+1, sumi, target)
            return dp[i][sumi]


        total = sum(nums) 
        if total % 2 != 0 :
            return False
        dp = [[-1]*(total//2 + 1) for _ in range(len(nums))]
        return f(0, 0, total//2)
        