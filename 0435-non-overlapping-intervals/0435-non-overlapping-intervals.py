from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        
        cnt = 1  # Start with the first interval (non-overlapping count)
        last_end_time = intervals[0][1]
        
        for i in range(1, n):
            # If the current interval starts after or at the end of the last interval
            if intervals[i][0] >= last_end_time:
                cnt += 1  # Include this interval
                last_end_time = intervals[i][1]
        
        # Total intervals - non-overlapping intervals = intervals to remove
        return n - cnt


