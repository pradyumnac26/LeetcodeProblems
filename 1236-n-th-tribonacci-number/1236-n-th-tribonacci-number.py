class Solution:
    def tribonacci(self, n: int) -> int:

        def f(i): 
            if i == 0 : 
                return 0 
            if i ==1 or i ==2 : 
                return 1 
            if dp[i] != -1 : 
                return dp[i]
            dp[i] = f(i-1) + f(i-2) + f(i-3)
            return dp[i]
        
        dp = [-1]*(n+1)
        return f(n)
        