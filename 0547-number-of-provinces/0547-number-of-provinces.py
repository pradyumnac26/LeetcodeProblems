class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node) : 
            visited[node] = True
            for nei in range(len(isConnected)): 
                if isConnected[node][nei] == 1 and visited[nei] != 1 : 
                    dfs(nei)




        visited = [False]*len(isConnected)
        cnt = 0 
        for i in range(len(isConnected)) : 
            if visited[i] == 0 : 

                cnt = cnt + 1
                dfs(i)
        return cnt



        