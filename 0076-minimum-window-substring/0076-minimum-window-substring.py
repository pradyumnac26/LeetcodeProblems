class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap2 = Counter(t) 
        l = 0 
        hmap1 = defaultdict(int) 
        minLen = float('inf')
        start = 0 

        def compare(hmap1, hmap2): 
            cnt = 0 
            for k,v in hmap2.items() : 
                if k in hmap1 and hmap1[k]>=v : 
                    cnt+=1 
            if cnt == len(hmap2) : 
                return True 
            else : 
                return False

        for r in range(len(s)): 
            hmap1[s[r]]+=1 
            while compare(hmap1,hmap2) :
                if (r-l+1) < minLen : 
                    minLen = r-l+1 
                    start = l
                
                hmap1[s[l]]-=1 
                l = l + 1
            
        if minLen == float('inf'):
            return ""

        return s[start:start + minLen]






        