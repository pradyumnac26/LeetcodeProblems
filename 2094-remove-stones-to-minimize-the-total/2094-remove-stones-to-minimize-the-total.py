class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-n for n in piles]
        heapq.heapify(max_heap)
        while k : 
            n = - heapq.heappop(max_heap)
            k = k -1
            heapq.heappush(max_heap, -math.ceil(n/2))
        
        x = 0 
        for i in range(len(max_heap)) : 
            x = x + abs(max_heap[i])
        return x 





        