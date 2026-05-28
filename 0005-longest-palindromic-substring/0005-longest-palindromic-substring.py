class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0] 
        maxi = 0
        if len(s) == 1 : 
            return s
         
        for k in range(len(s)): 
            i = k - 1 
            j = k + 1 
            while i >=0 and j < len(s) and s[i]==s[j] : 
                resLen = j-i+1 
                if resLen > maxi : 
                    maxi = resLen 
                    res = s[i: j+1] 
                i = i -1 
                j = j + 1 
            
            i = k 
            j = k+1 
            while i >=0 and j < len(s) and s[i]==s[j] : 
                resLen = j-i+1 
                if resLen > maxi : 
                    maxi = resLen 
                    res = s[i:j+1] 
                i = i -1 
                j = j +1 
        return res
            
                

            



        