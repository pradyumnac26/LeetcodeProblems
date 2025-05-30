class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {} 
        window = {} 
        res = [-1, -1]
        resLen = float('inf')
        l = 0 
        for i in range(len(t)): 
            c = t[i]
            countT[c] = 1 + countT.get(c,0) 
        
        have, need = 0, len(countT)
        for r in range(len(s)): 
            c = s[r]
            window[c] = window.get(c, 0) + 1 
            if c in countT and window[c] == countT[c] : 
                have = have + 1 

            while have == need : 
                if r-l+1 < resLen : 
                    res = [l,r]
                    resLen = r-l+1

                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]] : 
                    have = have -1  
                l = l + 1
        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""
         