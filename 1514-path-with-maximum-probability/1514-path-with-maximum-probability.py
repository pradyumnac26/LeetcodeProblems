class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        maxHeap = [] 
        adj = defaultdict(list) 
        for i, (u, v) in enumerate(edges) : 
            prob = succProb[i] 
            adj[u].append((v, prob)) 
            adj[v].append((u, prob))

        dist = [float("-inf")]*n 
        dist[start_node] = 1
        heapq.heappush(maxHeap, (-1, start_node)) 
        while maxHeap : 
            currprob, node = heapq.heappop(maxHeap)
            currprob = -currprob
            for nei, prob in adj[node] : 
                newprob = prob*currprob
                if newprob > dist[nei] : 
                    dist[nei] = newprob 
                    heapq.heappush(maxHeap, (-newprob, nei))
        ans = dist[end_node] 
        if ans == float("-inf") : 
            return 0 
        else : 
            return ans 


                





        