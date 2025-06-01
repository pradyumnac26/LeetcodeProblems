class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # adj list is already given.
        # bipartite means - even cycles , and can be bi-colored. odd cycle means it cant be bipartite.
        def bfs(node): 

            q = deque([node])
            color[node] = 1 # starting color is 1
            while q : 
                node = q.popleft()
                for nei in graph[node]: 
                    if color[nei]==-1: 
                        color[nei] = 1 - color[node]
                        q.append(nei)
                    elif color[nei] == color[node]: 
                        return False
            return True 


        n = len(graph)
        color = [-1]*n
        for i in range(n): 
            if color[i] == -1 : 
                if not bfs(i): 
                    return False
        return True 

        


        

        