class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        start = intervals[0][0]
        end = intervals[0][1]
        cnt = 0 
        for i in range(1, len(intervals)): 
            if start <= intervals[i][0] and  intervals[i][1] <=end  : 
                cnt +=1 
            else :
                start = intervals[i][0]
                end = intervals[i][1]

        return len(intervals) - cnt 

        