class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # connected, undirected and n cycles > tree 
        # node x as the root, 

        adj = defaultdict(list) 
        for u, v in edges : 
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, depth, vis, maxi) : 
            if node in vis : 
                return maxi
            vis.add(node)
            maxi = max(maxi, depth)
            for nei in adj[node] : 
                maxi = max(maxi, dfs(nei, depth+1, vis,maxi )) 
            return maxi




        res = [] 
        final = [] 
        mini = float('inf')

        for i in range(n):
            vis = set() 
            maxi = 0 
            res.append(dfs(i, 0, vis, maxi) )
        
        mini = min(res)
        for i in range(len(res)) : 
            if mini == res[i] : 
                final.append(i)
        return final 

            


        
        

        