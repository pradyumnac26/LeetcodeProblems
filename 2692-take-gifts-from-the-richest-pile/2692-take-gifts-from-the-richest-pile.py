class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = - gifts[i]
        
        heapq.heapify(gifts)
        for i in range(k):
            highest = -heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(sqrt(highest)))
        return -sum(gifts)

        