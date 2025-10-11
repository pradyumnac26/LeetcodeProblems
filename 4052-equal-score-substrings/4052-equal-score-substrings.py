class Solution:
    def scoreBalance(self, s: str) -> bool:
        for i in range(len(s)): 
            sumi1 = 0 
            sumi2 = 0 
            substring1 = s[:i+1] 
            substring2 = s[i+1:]
            for c in substring1 : 
                sumi1 = sumi1 + ord(c) - ord('a') + 1
            for c in substring2 : 
                sumi2 = sumi2 + ord(c) - ord('a') + 1 
            if sumi1 == sumi2 : 
                return True 
        return False 


