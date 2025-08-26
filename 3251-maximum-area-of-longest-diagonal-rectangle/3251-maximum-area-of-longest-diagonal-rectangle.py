class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # return the area of the rectangle having the longest diagonal. 
        # if there are multiple rectangles with the longest diagonal rectangle, return the area of the rectangle having the maximum area. 
        # first thing to do is find how to find the diagonal given the l and breadth of a rectangle. 
        # d = sqrt(l^2 + b^2)
        # find this for all the rectangles. and then retun the area which will be l*b for max rectangle. 
        # if there are more than 2 of the same, then return the area of the rectangle havig max area. 
        def computediagonal(l, b) : 
            return sqrt(l**2 + b**2)
        longest = 0
        for l, b in dimensions : 
            d = computediagonal(l, b)
            longest = max(longest, d)
        maxiarea = 0 
        for l, b in dimensions : 
            if computediagonal(l, b) == longest : 
                area = l*b
                maxiarea = max(area, maxiarea)
        return maxiarea






        