class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        l = 0 
        consec = 1 
        for r in range(len(nums)) : 
            if r > 0 and nums[r-1] + 1 == nums[r] : 
                consec +=1 
            
            if r-l+1 > k :
                if nums[l] + 1 == nums[l+1] : 
                    consec -= 1 
                l = l + 1

            if r-l+1 == k : 
                if consec == k : 
                    res.append(nums[r]) 
                else : 
                    res.append(-1)
        return res
             
        