class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap2 = Counter(t) 
        hmap1 = defaultdict(int) 
        # we need to check if all the elements in the t are there in the s, 
        # so i will count the characters in t, and as i move the window, i will have another hmap with all values in the window to check if we have the characters in t inside our s in the window, we need to dind a minimum substring.. 
        # second point is that so in that case we need to compare the 2 hmaps .. 
        mini = float('inf')
        start = 0 
        def compare(hmap1, hmap2) : 
            cnt = 0 
            for k, v in hmap2.items() : 
                if k in hmap1 and v <= hmap1[k] : 
                    cnt+=1 
            return cnt == len(hmap2)
        l = 0 
        for r in range(len(s)): 
            hmap1[s[r]]+=1 
            while compare(hmap1, hmap2) : 
                if r-l+1 < mini : 
                    mini = r-l+1 
                    start = l 
                hmap1[s[l]]-=1 
                if hmap1[s[l]] == 0 : 
                    del hmap1[s[l]] 
                l = l +1 
        
        if mini == float('inf'):
            return ""

        return s[start:start + mini]



        
        