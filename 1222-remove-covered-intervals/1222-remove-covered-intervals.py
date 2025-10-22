class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0 
        intervals.sort(key= lambda x: (x[0], -x[1]))
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for x, y in intervals[1:] : 
            if prev_start <= x and y<=prev_end : 
                cnt+=1 
            else : 
                prev_start = x 
                prev_end = y 
        return len(intervals) - cnt 
