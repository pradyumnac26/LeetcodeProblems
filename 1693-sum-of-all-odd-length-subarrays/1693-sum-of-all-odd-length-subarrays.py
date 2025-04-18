class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l,r = 0,0 
        sumi = 0 
        while l < len(arr): 
            for r in range(len(arr)): 
                if (r-l+1)%2 == 1 : 
                    sumi = sumi + sum(arr[l:r+1])
                    print(arr[l:r+1])
            l = l+1
        return sumi

        