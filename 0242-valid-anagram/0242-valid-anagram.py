class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = defaultdict(int) 
        for i in s : 
            hmap[i]+=1 
        for i in t : 
            if i in hmap : 
                hmap[i]-=1
            else : 
                return False 
        for v in hmap.values() : 
            if v != 0 : 
                return False 
        return True
        