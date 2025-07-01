class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges : 
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        for k, lis in adj.items() : 
            if len(lis) >= 2 : 
                return k

        