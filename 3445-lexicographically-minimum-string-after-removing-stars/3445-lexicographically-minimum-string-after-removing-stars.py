class Solution:
    def clearStars(self, s: str) -> str:
        minHeap = [] 
        n = len(s)
        mask = [True]*n
        x = ""
        if "*" not in s : 
            return s
        for i, ch in enumerate(s) : 
            if ch != "*": 
                heapq.heappush(minHeap, (ch, -i))
            else : 
                mini, ind = heapq.heappop(minHeap)
                neg_ind = -ind
                mask[i] = False
                mask[neg_ind] = False
        for i in range(n): 
            if mask[i] : 
                x = x + s[i]
            else : 
                x = x + ""
        return x 

        