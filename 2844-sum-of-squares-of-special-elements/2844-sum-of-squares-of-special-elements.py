class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        cnt = 0 
        n = len(nums)
        for i in range(1, n+1) : 
            if n%i == 0 : 
                cnt = cnt + nums[i-1]*nums[i-1]
        return cnt 

        