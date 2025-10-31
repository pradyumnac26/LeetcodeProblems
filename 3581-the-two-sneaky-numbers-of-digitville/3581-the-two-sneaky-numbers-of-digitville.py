class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = [] 
        vis = set() 
        for i in nums : 
            if i not in vis : 
                vis.add(i) 
            else : 
                res.append(i)
        return res
        
        