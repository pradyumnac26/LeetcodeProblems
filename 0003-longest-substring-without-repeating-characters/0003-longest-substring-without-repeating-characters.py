class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {} 
        l = 0 
        cnt = 0 
        for r in range(len(s)): 
            hmap[s[r]] = 1 + hmap.get(s[r], 0) 
            while hmap[s[r]] > 1 : 
                hmap[s[l]] -= 1 
                if hmap[s[l]] == 0 : 
                    del hmap[s[l]]
                l+=1 
            cnt = max(cnt, r-l+1)
        return cnt
            


        