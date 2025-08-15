class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1 : 
            return False
        while n > 1 : 
            n = n/3 
        return n==1 