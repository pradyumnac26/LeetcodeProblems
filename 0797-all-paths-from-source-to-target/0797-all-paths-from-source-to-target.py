class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        target = len(graph) - 1

        def dfs(node, path):
            if node == target:
                res.append(path[:])
                return
            for neighbor in graph[node]:
                dfs(neighbor, path + [neighbor])

        dfs(0, [0])
        return res
