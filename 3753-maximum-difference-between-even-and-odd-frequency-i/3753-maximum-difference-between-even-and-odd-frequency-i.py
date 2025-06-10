class Solution:
    def maxDifference(self, s: str) -> int:
        # given a string s, consisting of lowercase letters.
        # find the max difference a1-a2 between frequency of charcters a1 and a2, where a1 is odd freq and a2 is even freq.
        hmap = {}
        maxeven = 0 
        maxodd = 0
        maxi = float('-inf')  
        for i in range(len(s)):
            hmap[s[i]] = 1 + hmap.get(s[i], 0 )
            
        for k, v in hmap.items(): 
            if v % 2 == 0: 
                maxeven = max(maxeven, v)
            else : 
                maxodd = max(maxodd, v)
        
        if maxeven == 0 or maxodd == 0 : 
            return -1 
        else : 
            maxi = max(maxi, maxodd-maxeven)
            return maxi

 




        