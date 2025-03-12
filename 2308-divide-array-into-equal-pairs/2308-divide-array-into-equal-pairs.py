class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2 != 0 : 
            return False
        
        hmap = Counter(nums)
        for i,j in hmap.items(): 
            if j%2 != 0 : 
                return False
        return True
        