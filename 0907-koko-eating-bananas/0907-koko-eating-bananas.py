class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def func(arr, k) : 
            totalHrs = 0 
            for i in range(len(arr)):
                totalHrs += math.ceil((arr[i]) / k)
            return totalHrs
        
        low = 1 
        high = max(piles) 
        while low <= high : 
            mid = (low + high) // 2 
            totalHrs = func(piles, mid)
            if totalHrs <= h : 
                high = mid - 1 
            else : 
                low = mid + 1
        return low


        