class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = [] 
        for u,v in tasks : 
            res.append(u+v)
        return min(res)
        