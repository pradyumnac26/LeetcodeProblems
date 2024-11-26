class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay) 
        if n < m*k : 
            return -1

        def possible(arr, day, m, k):
            cnt = 0 
            noBouquets = 0 
            for i in range(len(arr)) : 
                if arr[i] <= day : 
                    cnt += 1
                else : 
                    noBouquets += cnt//k
                    cnt = 0 
            noBouquets += cnt//k
            if noBouquets >= m : 
                return True
            else : 
                return False






        low, high = min(bloomDay), max(bloomDay)

        while low <= high : 
            mid = (low + high )//2 
            if (possible(bloomDay, mid, m,k) == True) : 
                high = mid -1 
            else : 
                low = mid +1 
        return low 
        