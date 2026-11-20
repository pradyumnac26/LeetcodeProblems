class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        def dist(x1, y1, x2, y2) : 
            return math.sqrt((x1-x2)**2 + (y1-y2)**2) 
        res = [] 
        for c1, c2, r in queries : 
            cnt = 0 
            for p1, p2 in points : 
                if (p1-c1)**2 + (p2-c2)**2 <= r*r: 
                    cnt+=1 
            res.append(cnt)
        return res
        