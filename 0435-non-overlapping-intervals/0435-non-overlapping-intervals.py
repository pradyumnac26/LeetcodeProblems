class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1,2], [1, 3], [2, 3], [3, 4]
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < last_end:
                cnt += 1
            else:
                last_end = end

        return cnt

        