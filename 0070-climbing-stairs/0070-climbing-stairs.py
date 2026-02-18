class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def f(i) : 
            if i <= 1 : 
                return 1 
            left = f(i-1)
            right = f(i-2)
            return left + right 

        return f(n)

        