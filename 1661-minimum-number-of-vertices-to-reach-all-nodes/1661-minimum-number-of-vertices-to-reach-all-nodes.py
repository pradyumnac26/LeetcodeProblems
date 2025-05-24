class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # min number of vertices to reach all node. 
        # i convert to adj list 0: [1, 2] , 1 : [] , 2 : [5], 3: [4], 4: [2], 5:[]
        # so in a DAG the nodes which are unreachable are th nodes with indegree = 0. corect. 
        # so the min number of nodes to reach all nodes = number of nodes with indegree = 0 

        x = [] 
        indegree = [0]*n 
        for u, v in edges : 
            indegree[v] += 1
        cnt = 0
        for i in range(n): 
            if indegree[i]==0 : 
                x.append(i)
        return x
            


        