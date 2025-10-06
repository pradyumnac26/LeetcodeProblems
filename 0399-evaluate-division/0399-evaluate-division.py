from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for idx, (u, v) in enumerate(equations):
            adj[u].append((v, values[idx]))       # u / v = values[idx]
            adj[v].append((u, 1 / values[idx]))   # v / u = 1 / values[idx]

        # Step 2: Define DFS
        def dfs(node, target, value):
            if node == target:
                return value
            vis.add(node)
            for nei, wt in adj[node]:
                if nei not in vis:
                    ans = dfs(nei, target, value * wt)
                    if ans != -1:
                        return ans
            return -1

        # Step 3: Answer each query
        res = []
        for node, target in queries:
            if node not in adj or target not in adj:
                res.append(-1.0)
                continue
            vis = set()
            ans = dfs(node, target, 1)
            res.append(ans)
        return res
