class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = [] 
        end = [] 
        for x,y in intervals : 
            start.append(x)
            end.append(y)
        start.sort()
        end.sort() 
        i = 0 
        j = 0 
        res = 0
        maxi = 0
        while i < len(start) and j < len(end) :  
            if start[i] < end[j] : 
                res +=1 
                i = i + 1 
            else : 
                res-=1 
                j = j + 1 
            maxi = max(maxi, res)
        return res



        