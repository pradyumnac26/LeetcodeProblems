from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        deg = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # start with all leaves
        q = deque([i for i in range(n) if deg[i] == 1])
        remaining = n

        # peel leaves layer by layer
        while remaining > 2:
            layer_size = len(q)
            remaining -= layer_size

            for _ in range(layer_size):
                leaf = q.popleft()
                for nei in adj[leaf]:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        q.append(nei)

        return list(q)
