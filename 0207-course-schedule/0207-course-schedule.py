class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort 
        q = deque()
        indegree = [0]*numCourses
        adj = defaultdict(list)
        for u, v in prerequisites : 
            adj[v].append(u)
            indegree[u]+=1
        print(adj, indegree)
        q = deque()
        for node, deg in enumerate(indegree): 
            if deg == 0 : 
                q.append(node)
        res = [] 
        while q : 
            node = q.popleft() 
            res.append(node)
            for nei in adj[node] :
                indegree[nei]-=1 
                if indegree[nei] == 0 : 
                    q.append(nei)
        if len(res) == numCourses : 
            return True 
        else : 
            return False


            
            

        

        