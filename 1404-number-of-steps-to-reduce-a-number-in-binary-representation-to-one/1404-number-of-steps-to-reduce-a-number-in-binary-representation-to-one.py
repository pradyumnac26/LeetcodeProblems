class Solution:
    def numSteps(self, s: str) -> int:
        x = int(s, 2) 
        st = 0
        while x > 1 : 
            if x%2 == 0 : 
                x = x//2 
            else : 
                x = x + 1 
            st+=1 
        return st