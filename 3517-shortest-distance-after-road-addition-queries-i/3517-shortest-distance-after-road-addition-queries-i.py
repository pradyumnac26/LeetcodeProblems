class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [] 
        res = []




        for i in range(n) : 
            adj.append([i+1])

        def shortest_path() :
            q = deque()
            visited = set()
            q.append((0,0)) #node, length
            visited.add((0,0))
            while len(q) > 0 : 
                cur,length = q.popleft()
                if cur == n-1 : 
                    return length
                for nei in adj[cur] : 
                    if nei not in visited : 
                        q.append((nei, length+1))
                        visited.add(nei)

        
        for src,dst in queries : 
            adj[src].append(dst)
            res.append(shortest_path())
        return res

        



        