class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1,2], [1, 3], [2, 3], [3, 4]
        intervals.sort() 
        cnt = 0 
        res = [intervals[0]]
        for start, end in intervals[1:] : 
            if start < res[-1][1] : 
                cnt+=1 
                res[-1][1] = min(res[-1][1], end)
            else : 
                res.append([start, end])
        return cnt


        