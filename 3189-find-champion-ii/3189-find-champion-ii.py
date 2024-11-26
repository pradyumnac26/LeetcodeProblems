class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0]*n
        ans = [] 
        for src, dst in edges : 
            incoming[dst] += 1
    
        for i,incoming_cnt in enumerate(incoming) : 
            if not incoming_cnt : 
                ans.append(i)

        
        if len(ans) > 1 : 
            return -1 
        else : 
            return ans[0]
            

        