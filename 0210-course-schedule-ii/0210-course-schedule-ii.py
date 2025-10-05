class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topo sort ordering. 
        indegree = [0]*numCourses 
        q = deque()
        adj = defaultdict(list) 
        for u, v in prerequisites : 
            adj[v].append(u)
            indegree[u] +=1

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
        return res if len(res) == numCourses else []      