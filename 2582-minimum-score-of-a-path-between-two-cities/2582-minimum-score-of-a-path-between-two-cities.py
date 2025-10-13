class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list) 
        score = float('inf') 
        for u, v, dist in roads : 
            adj[u].append((v, dist))
            adj[v].append((u, dist))
        print(adj)
        def dfs(node): 
            nonlocal score 
            if node in vis : 
                return 
            vis.add(node)
            for nei, d in adj[node]: 

                score = min(score, d)
                dfs(nei)


        vis = set()

        dfs(1)

        return score
        