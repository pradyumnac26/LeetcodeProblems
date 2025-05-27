class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # adjacency list already given
        # cycle detectio ina directed graph.
        visited = [False]*len(rooms)
        def dfs(node): 
            visited[node] = True 
            for nei in rooms[node]: 
                if not visited[nei]: 
                    dfs(nei)
            
        dfs(0)
        return all(visited)



        