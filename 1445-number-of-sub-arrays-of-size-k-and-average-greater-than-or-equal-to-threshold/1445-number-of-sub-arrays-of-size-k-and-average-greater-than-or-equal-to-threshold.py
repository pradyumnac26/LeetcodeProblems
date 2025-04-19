class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0 
        r = k 
        windowsum = sum(arr[:k])
        target = k*threshold
        count = 0 
        if windowsum >= target : 
            count = count + 1

        while r < len(arr): 
            windowsum = windowsum - arr[l] + arr[r]
            if windowsum >= target : 
                count = count +1
            l = l+1
            r = r+1
        return count 

        