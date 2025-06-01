class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dist = [float('inf')]*n
        dist[src] = 0 
        for _ in range(k+1): 
            prev = dist[:]
            for u,v,w in flights : 
                if prev[u] + w < dist[v] : 
                    dist[v] = prev[u] + w
        return -1 if dist[dst] == float('inf') else dist[dst]








        