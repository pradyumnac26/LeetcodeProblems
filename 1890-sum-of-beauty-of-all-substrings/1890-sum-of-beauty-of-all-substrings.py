class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0 
        for i in range(len(s)) : 
            hmap = defaultdict(int) 
            for j in range(i,len(s)) : 
                hmap[s[j]]+=1

                max_freq = max(hmap.values())
                min_freq = min(hmap.values())

                beauty += (max_freq - min_freq) 

        return beauty







        