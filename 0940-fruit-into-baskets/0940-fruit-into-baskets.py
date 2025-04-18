class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        r, l = 0,0 
        maxlen = 0 
        hmap = defaultdict(int)
        for r in range(len(fruits)) : 
            hmap[fruits[r]] += 1 
            while len(hmap) > 2 : 
                hmap[fruits[l]] -=1
                if hmap[fruits[l]] == 0 : 
                    del hmap[fruits[l]]
                l = l + 1
            maxlen = max(maxlen, r-l+1)
        return maxlen


            
        
        