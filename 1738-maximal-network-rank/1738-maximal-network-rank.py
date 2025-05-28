class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        outdegree = [0] * n
        for u, v in roads:
            adj[u].add(v)
            outdegree[u] += 1
            adj[v].add(u)
            outdegree[v] += 1
        res = -inf
        for i in range(n):
            for j in range(i + 1, n):
                curr = outdegree[i] + outdegree[j]
                if j in adj[i]:
                    curr -= 1
                res = max(res, curr)
        return res