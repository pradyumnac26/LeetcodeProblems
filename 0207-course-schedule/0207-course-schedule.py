class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort 
        adj = defaultdict(list)
        q = deque() 
        res = [] 
        indegree = [0]*numCourses
        for u, v in prerequisites : 
            adj[v].append(u) 
            indegree[u]+=1 
        for i in range(len(indegree)) : 
            if indegree[i] == 0 : 
                q.append(i)
        while q : 
            node = q.popleft() 
            res.append(node)
            for nei in adj[node]: 
                indegree[nei]-=1 
                if indegree[nei] == 0 : 
                    q.append(nei)
        if len(res) == numCourses : 
            return True 
        else : 
            return False

        


        

        