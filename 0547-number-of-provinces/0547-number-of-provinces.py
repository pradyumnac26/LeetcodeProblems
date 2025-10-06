class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list) 
        rows, cols = len(isConnected), len(isConnected)
        edges = []
        vis = set()
        for i in range(rows) :
            for j in range(i+1, cols) : 
                if i != j and isConnected[i][j] == 1: 
                    edges.append((i+1, j+1))

        for u, v in edges : 
            adj[u].append(v)
            adj[v].append(u)
        for i in range(1, rows+1) : 
            if i not in adj : 
                adj[i] = []
        print(adj)

        def dfs(node) : 
            if node in vis : 
                return 
            vis.add(node) 
            for nei in adj[node]: 
                dfs(nei)

        cnt = 0 
        for i in range(1, rows+1) : 
            if i not in vis : 
                dfs(i)
                cnt+=1 
        return cnt

