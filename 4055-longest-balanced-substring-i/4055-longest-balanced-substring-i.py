class Solution:
    def longestBalanced(self, s: str) -> int:
        maxi = 0 
        for i in range(len(s)): 
            hmap = defaultdict(int)
            for j in range(i, len(s)): 
                hmap[s[j]] +=1 
                if len(set(hmap.values())) == 1 : 
                    maxi = max(maxi, j-i+1)
        return maxi


        