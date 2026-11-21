class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) 
        for u, v, w in times : 
            adj[u].append((v, w)) 

        dist = [float("inf")]*(n+1) 
        dist[k] = 0
        minHeap = [] 
        heapq.heappush(minHeap, (0,k))
        while minHeap : 
            currdist, node = heapq.heappop(minHeap)
            for nei, w in adj[node] : 
                newdist = currdist + w
                if newdist < dist[nei] : 
                    dist[nei] = newdist 
                    heapq.heappush(minHeap, (newdist, nei))

        ans = max(dist[1:])
        if ans != float("inf") : 
            return ans 
        else : 
            return -1
        
                    

