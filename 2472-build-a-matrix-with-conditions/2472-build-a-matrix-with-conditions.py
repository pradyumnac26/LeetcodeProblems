class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topo_sort(adj, indegree): 
            q = deque()
            topo = [] 
            for i in range(1, k+1): 
                if indegree[i] == 0 : 
                    q.append(i)
            while q : 
                node = q.popleft()
                topo.append(node)
                for nei in adj[node]: 
                    indegree[nei]-=1
                    if indegree[nei] == 0 : 
                        q.append(nei)
            return topo

        adjrow = defaultdict(list)
        adjcol = defaultdict(list)
        indegreerow = [0]*(k+1)
        indegreecol = [0]*(k+1)
        for u,v in rowConditions: 
            adjrow[u].append(v)
            indegreerow[v] +=1
        for u, v in colConditions: 
            adjcol[u].append(v)
            indegreecol[v] +=1

        topo1 = topo_sort(adjrow, indegreerow[:])
        topo2 = topo_sort(adjcol, indegreecol[:])
        print(topo1)
        print(topo2)
        if len(topo1) < k or len(topo2) < k:
            return []

        matrix = [[0]*k for _ in range(k)]
        row_pos = {} 
        col_pos = {} 
        for i, num in enumerate(topo1): 
            row_pos[num] = i 

        for i, num in enumerate(topo2): 
            col_pos[num] = i 

        for ind in range(1, k+1): 
            r = row_pos[ind]
            c = col_pos[ind]
            matrix[r][c] = ind
        return matrix

            






        
        
        


        