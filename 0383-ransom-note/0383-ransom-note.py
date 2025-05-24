class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)
        for i in ransomNote : 
            hmap1[i] += 1
        print(hmap1)
        for j in magazine : 
            hmap2[j] +=1
        print(hmap2)

        for k,v in hmap1.items() : 
            if hmap2[k] < v : 
                return False
        return True

        