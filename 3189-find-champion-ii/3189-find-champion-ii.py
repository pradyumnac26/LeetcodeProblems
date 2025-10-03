class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list) 
        indegree = [0]*n 
        cnt = 0
        tmp =0
        for u, v in edges : 
            indegree[v] +=1
        for i in range(len(indegree)): 
            if indegree[i] == 0 : 
                cnt+=1 
                tmp = i
        if cnt > 1 : 
            return -1 
        else : 
            return tmp


        