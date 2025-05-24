class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # given a/b as 2 and b/c as 3, so a = 2b and b = 3c.
        # a/c = a/b * b/c = 6 
        # a ->b weight = 2, b- >c weight as 3. -> 6 
        # 

        adj = defaultdict(list)
        for i in range(len(equations)): 
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1/values[i]))
        print(adj)



        def dfs(src, dst, vis, adj, prod):

            if src not in adj or dst not in adj : 
                return -1
            if src == dst : 
                return prod

            vis.add(src)
            for nei, wt in adj[src] : 
                if nei not in vis : 
                   result =  dfs(nei, dst,vis,  adj, prod*wt)
                   if result != -1: 
                        return result 

            return -1
                



            
            
            


        res = [] 
        vis = set()
        for i in range(len(queries)): 
            res.append(dfs(queries[i][0], queries[i][1], set(), adj, 1))
        return res

            



        
        