class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(g)
        n = len(s)
        l,r = 0,0 
        g.sort()
        s.sort()
        while l<n and r<m: 
            if g[r] <= s[l] : 
                r = r + 1 
            l = l +1 
        return r


        