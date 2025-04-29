class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = 0
        while l <= r : 
            mid = (l + r)//2 
            sumi = 0 
            cnt = 1 
            for i in range(len(weights)) : 
                sumi = sumi + weights[i]
                if sumi > mid :
                    cnt = cnt + 1 
                    sumi = weights[i] 
            if cnt <= days : 
                ans = mid
                r = mid - 1 
            else : 
                l = mid + 1 
        return ans
        






        