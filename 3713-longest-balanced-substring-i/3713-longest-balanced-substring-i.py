class Solution:
    def longestBalanced(self, s: str) -> int:
        # if all distinct characters in the substring the same number of times, then it is then we need to return the length of the longest balanced substring... 
        # z = 2, a = 1, b = 1, c = 1, simultaneously we see if there are any values with the same number of occurecnece. and simltaneouslt cal the length 

        maxi = 0 
        for i in range(len(s)): 
            hmap = {} 

            for j in range(i, len(s)) : 
                hmap[s[j]] = 1 + hmap.get(s[j], 0)
                if len(set(hmap.values())) <= 1 : 
                    maxi = max(maxi, j-i+1)
        return maxi




        