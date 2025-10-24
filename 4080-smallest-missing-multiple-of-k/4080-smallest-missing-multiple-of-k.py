class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        flag = True
        x = 2
        if k not in s : 
            return k 
        while flag : 
            z = k*x
            x = x + 1
            if z not in s:
                flag = False 
        return z


        