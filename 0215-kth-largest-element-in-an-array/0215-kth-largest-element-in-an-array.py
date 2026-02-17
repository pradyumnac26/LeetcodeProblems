class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest element in the array.. 
        # sort and then return the n-kth element , or sort descdning and returna and then return k-1th element.. 
        # but without sorting how to do it .?? 
        # first lets solve using a minHeap 

        minHeap = [] 

        for i in nums : 
            heapq.heappush(minHeap, i) 
            if len(minHeap) > k : 
                heapq.heappop(minHeap)
        return heapq.heappop(minHeap)


        