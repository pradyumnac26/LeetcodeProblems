class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" 
        resLen =0 
        startIdx = 0 
        for i in range(len(s)) : 
            l, r = i, i 
            while l >=0 and r < len(s) and s[l] == s[r] : 
                if (r - l +1) >  resLen : 
                    resLen = r-l+1 
                    startIdx = l 
                l = l -1 
                r = r + 1 

            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r] : 
                if (r-l+1) > resLen : 
                    resLen = r - l + 1 
                    startIdx = l 
                l = l -1 
                r = r + 1 
        return s[startIdx: startIdx+resLen]



        

        
        