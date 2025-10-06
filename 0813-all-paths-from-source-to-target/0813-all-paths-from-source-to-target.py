class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path.copy())
                return
            for nei in graph[node]:
                path.append(nei)     # \U0001f448 add next node before exploring
                dfs(nei, path)
                path.pop()           # \U0001f448 backtrack after returning

        res = []
        dfs(0, [0])                  # \U0001f448 start with [0] as initial path
        return res


        