class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # number of complete connected components. 
        # first build adj list. 
        # 2. run a dfs and kep trackof the number of connected components. 
        # 3. while taking a cnt, how will we check if it is complete ? 
        # we need to run a dfs nd check if it returns back to the strting point ? 
        # 
        adj = defaultdict(list) 
        for u, v in edges : 
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        def dfs(node, n_nodes, n_edges): 

            vis.add(node) 
            n_nodes +=1
            n_edges += len(adj[node])
            for nei in adj[node]: 
                if nei not in vis : 
                    n_nodes, n_edges = dfs(nei, n_nodes, n_edges)
            return n_nodes, n_edges

        res = [False]
        vis = set()
        cnt = 0
        n_nodes = 0 
        n_edges = 0 
        for i in range(n): 
            if i not in vis : 
                totalnodes, totaledges = dfs(i, n_nodes, n_edges)
                totaledges = totaledges//2
                if totaledges == (totalnodes*(totalnodes-1))//2 : 
                    cnt+=1 
        return cnt


        