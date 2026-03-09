class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # return the height of min heights root label  
        # so first i will try with 0 as root, so go bfs and measure the height till the last node. 
        # then try from 1 , and then try from 2, and then try from 3.. 
        adj = defaultdict(list)
        indegree = [0]*n
        for u, v in edges : 
            adj[u].append(v) 
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        print(adj)
        if n == 1:
            return [0]

        q = deque()
        for i in range(n): 
            if indegree[i] == 1 : 
                q.append(i)
        remaining_nodes = n 
        while remaining_nodes > 2 : 
            leaf_count = len(q) 
            remaining_nodes -= leaf_count
            for _ in range(leaf_count): 
                node = q.popleft()
                for nei in adj[node]:
                    indegree[nei]-=1 
                    if indegree[nei] == 1 : 
                        q.append(nei)
        return list(q)
        





        