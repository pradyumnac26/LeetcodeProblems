class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # n - (number of overlapping intervals )
        points.sort(key = lambda x: x[1])
        print(points)
        start = points[0][0]
        end = points[0][1]
        cnt = 0 
        for i in range(1, len(points)): 
            if end >= points[i][0]: 
                cnt = cnt + 1 
                end = min(points[i][1], end)
            else : 
                end = points[i][1]
        return len(points)-cnt

