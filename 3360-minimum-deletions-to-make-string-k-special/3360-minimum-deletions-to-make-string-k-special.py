class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        hmap = Counter(word)
        print(hmap)
        res = float('inf')
        for low in hmap.values(): 
            destroy = 0 
            for v in hmap.values(): 
                if v < low : 
                    destroy += v
                elif v > low + k : 
                    destroy += v - (low+k)
            res = min(res, destroy)
        return res
                

        
        