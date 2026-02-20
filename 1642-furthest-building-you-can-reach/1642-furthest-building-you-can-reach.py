class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # given an integer array heights of the buildings bricks, and ladders
        # so say if height[i+1] > height[i] then can use 1 ladder or height[i+1] - height[i] number of bricks 
        # but we neeed to return the maximum building it can reach 
        # so here at each point we have 2 choices for bricks or laders, so we can try all ways.. 
        # for largest diff we want to add ladder... 
        minHeap = [] 
        for i in range(len(heights)-1) : 
            d = heights[i+1] - heights[i] 
            if d <=0 : 
                continue 
            heapq.heappush(minHeap, d)
            if len(minHeap) > ladders : 
                bricks = bricks - heapq.heappop(minHeap)
            if bricks < 0 : 
                return i 
        return len(heights)-1



            


                        

        