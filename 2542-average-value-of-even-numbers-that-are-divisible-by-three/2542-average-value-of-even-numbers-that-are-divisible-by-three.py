class Solution:
    def averageValue(self, nums: List[int]) -> int:
        b = [] 
        for i in nums : 
            if i % 6 == 0 : 
                b.append(i)
        if len(b) == 0 :
            return 0
        return sum(b) // len(b)
                

        