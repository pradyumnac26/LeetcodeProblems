class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # at most twice repeated. 
        res = [] 
        for n in nums : 
            idx = abs(n)-1
            if nums[idx] < 0 : 
                res.append(abs(n))
            else : 
                nums[idx] = -nums[idx]
        return res

        