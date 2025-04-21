class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # keep a fixed window of size 3 and add all of them to the hmap using counter or something.
        # later, slide the window , then reduce the count in hmap and do l+1. 
        # so say xyzzaz here x:1, y:1, z:1 if len(hmap)==3 : cnt = cnt +1 , l = l+1, hmap[nums[l]]-=1, if == 0 then del.
        r = 0
        l = 0 
        cnt = 0 
        hmap = defaultdict(int)

        n = len(s)
        for r in range(n): 
            hmap[s[r]]+=1
            while r-l+1 > 3 : 
                hmap[s[l]]-=1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
                l = l+1
                
            if len(hmap)==3 and r-l+1 == 3 : 
                cnt = cnt + 1  

        return cnt
          

        