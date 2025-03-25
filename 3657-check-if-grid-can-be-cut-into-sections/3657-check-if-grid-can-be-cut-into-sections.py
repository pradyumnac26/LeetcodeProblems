class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # so first let me read the problem and understand and try coming up with an algorithm . step by step
        # so n is the dimensions of the grid and rectangles determin the rectanges inside the grid with their start and end points.
        # say first i iterate to start marking rectabges 
        # in rectangles[i][0] = startx; rectangles[i][1] = starty, rectangles[i][2] = endx; rectangles[i][3] = endy 
        # so now we can calculatte the height of the rectangle by saying that endy - starty. 
        # i think this is turning out to be lie an interval problem.
        # say i start puting the starty, endy in another list , so [0,2] and then [2,4] and then [2,3] and then [4,5]
        # so from this we need to find that there are atleasr 3 rectangles which are not overlapping (inclusibely)
        # so now broke down the problem to this , this list - [[0,2],[2,4],[2,3], [4,5]], we need to have a total of just 3 lits sinside this. 
        # wait so now this was jsut for the horizontal cuts , and for the horizontal cuts u need to do for startx, endx.
        # so we need to check both and output true or false. 
        # now lets start coding. 
        hor = []
        ver = []
        for i in range(len(rectangles)) : 
            startx, starty , endx, endy = rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3]
            hor.append([startx, endx])
            ver.append([starty, endy])
        print(hor)
        print(ver)
        
        hor.sort()

        hor_groups = []
        for i in range(len(hor)) : 
            start, end = hor[i][0], hor[i][1]
            if hor_groups and start < hor_groups[-1][1] : 
                hor_groups[-1][1] = max(hor_groups[-1][1], end )
            else : 
                hor_groups.append([start, end ])

        if len(hor_groups) >= 3:
            return True

        ver.sort()
        ver_groups = []

        for i in range(len(ver)):
            start, end = ver[i][0], ver[i][1]
            if ver_groups and start < ver_groups[-1][1]:
                ver_groups[-1][1] = max(ver_groups[-1][1], end)
            else:
                ver_groups.append([start, end])
        if len(ver_groups) >= 3:
            return True
        
        return False



        



        