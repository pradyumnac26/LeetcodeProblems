from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)
        
        for src, dst in edges:
            adj[src].append(dst)
        
        # Track visited and recursion stack for cycle detection
        visit = set()
        path = set()

        # count[node][c] = max frequency of color c on a path ending at node
        count = [[0] * 26 for _ in range(n)]

        def dfs(node):
            if node in path:
                return float('inf')  # cycle detected
            if node in visit:
                return 0  # already processed

            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] = 1  # self contributes 1 to its own color

            for nei in adj[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')  # propagate cycle

                for c in range(26):
                    # take the max from neighbor, plus 1 if this node adds to the color
                    count[node][c] = max(
                        count[node][c],
                        count[nei][c] + (1 if c == colorIndex else 0)
                    )

            path.remove(node)  # remove from recursion stack
            return 0

        res = 0
        for i in range(n):
            if dfs(i) == float('inf'):
                return -1
            res = max(res, max(count[i]))

        return res
