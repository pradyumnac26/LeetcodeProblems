class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = [] # endtime, number of passengers
        trips.sort(key=lambda x : x[1])
        curPass = 0 
        for t in trips : 
            numPass, start, end = t
            while minHeap and start >= minHeap[0][0]: 
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)


            curPass += numPass
            if curPass > capacity : 
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True 

            




        