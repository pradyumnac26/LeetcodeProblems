class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0 
        l = 0 
        for r in range(len(s)) : 
            if s[r] == "0" : 
                res = res + (r-l)
                l = l+1 
        return res
        
        
        