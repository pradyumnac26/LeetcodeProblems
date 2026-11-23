class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list) 
        for u, v, dist in edges : 
            adj[u].append((v, dist)) 
            adj[v].append((u, dist))
         
        def djiktras(src) : 
            minHeap = [(0, src)] # dist, src 
            visited = set() 

            while minHeap : 
                dist, node = heapq.heappop(minHeap) 
                if node in visited : 
                    continue
                
                visited.add(node)

                for nei, dist1 in adj[node] : 
                    newdist = dist + dist1 
                    if newdist <= distanceThreshold : 
                        heapq.heappush(minHeap, (newdist, nei))
            return len(visited)-1



        res = [] 
        for src in range(n) :  
            count = djiktras(src)
            res.append(count) 
        mini = min(res)
        for i in range(len(res)-1, -1, -1) : 
            if res[i] == mini : 
                return i





        