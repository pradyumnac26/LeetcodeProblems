class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque() 
        minHeap = [] 
        t = 0
        cnt = Counter(tasks)
        for k, v in cnt.items() : 
            heapq.heappush(minHeap, -v)
        
        while minHeap or q : 
            t = t+1
            if minHeap : 
                x = -heapq.heappop(minHeap)
                x = x - 1
                if x > 0 : 
                    q.append((x, t+n))
                
            if q and q[0][1] == t : 
                cnt, _ = q.popleft()
                heapq.heappush(minHeap, -cnt)
        return t
                
            

        


        