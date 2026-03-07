class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(1, len(isConnected)+1): 
            for j in range(1, len(isConnected)+1): 
                if i!=j and isConnected[i-1][j-1] == 1: 
                    adj[i].append(j)
        print(adj)

        def dfs(i) : 
            if i > len(isConnected): 
                return
            if i in vis : 
                return 
            vis.add(i)
            for nei in adj[i] : 
                dfs(nei)
        
        vis = set()
        cnt = 0 
        for i in range(1, len(isConnected)+1) :
            if i not in vis : 
                dfs(i) 
                cnt+=1 
        return cnt



        