class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        indegree = [0]*n
        topo = []
        adj = defaultdict(list)
        for dst, src in prerequisites : 
            indegree[dst]+=1
            adj[src].append(dst)

        q = deque()
        for i in range(n): 
            if indegree[i] == 0 : 
                q.append(i)

        while q: 
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]: 
                    indegree[nei]-=1
                    if indegree[nei] == 0 : 
                        q.append(nei)
        return topo if len(topo) == numCourses else []




        