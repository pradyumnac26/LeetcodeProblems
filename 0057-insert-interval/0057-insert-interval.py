class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])  # ensure sorted by start

        res = [intervals[0]]

        for start, end in intervals[1:]:
            # compare with the last interval in result
            if res[-1][1] >= start:  # overlap
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res


