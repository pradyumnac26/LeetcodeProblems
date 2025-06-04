class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        maxi = 0
        for u,v in connections : 
            adj[u].append(v)
            adj[v].append(u)
     
        
        if len(connections) < n-1 : 
            return -1

        visited = [False]*n
        def dfs(node): 
            visited[node] = 1
            for nei in adj[node]: 
                if not visited[nei]: 
                    dfs(nei)



        count = 0 
        for i in range(n): 
            if not visited[i]: 
                dfs(i)
                count +=1 
        return count -1
        
