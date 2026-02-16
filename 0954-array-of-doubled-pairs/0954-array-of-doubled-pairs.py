class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # arr is even length 
        # return true if it is possible to reorder arr such that 
        # arr[2*i+1] = 2*arr[2*i] for every i in 0betwee n 0 and the mid of array.. 
        # meaning lets break this down..to make some observations.. [a, b, c, d, e, f]
        # i = 0 => arr[1] = 2*arr[0] 
        # i = 1 => arr[3] = 2*arr[2] 
        # i = 2 => arr[5] = 2*arr[4] 
        # so we need to see if theat double is there in the array, and if all such pairs are there then we return ttrue. 
        # reorder such that every second element
        n = len(arr)//2
        cnt = 0 
        hmap = Counter(arr)
        print(hmap)
        if len(arr) == 2 : 
            if arr[0] == 0 and arr[1] == 0 : 
                return True
            if arr[0] == 0 or arr[1] == 0 : 
                return False 
        for i in sorted(arr) : 
            if i in hmap and 2*i in hmap : 
                hmap[2*i]-=1 
                hmap[i]-=1
                cnt+=1
                if hmap[2*i] <= 0 : 
                    del hmap[2*i]
                if hmap[i] <= 0 : 
                    del hmap[i]
        print(hmap)
        print(cnt)
        if cnt == n : 
            return True 
        else : 
            return False




            



        