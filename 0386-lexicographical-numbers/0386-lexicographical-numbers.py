class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # lexographical ordering of numbers
        res = []
        def dfs(cur): 
            if cur > n : 
                return 
            res.append(cur)
            cur=cur*10
            for i in range(10): 
                dfs(cur+i)

        
        for i in range(1, 10): 
            dfs(i)
        return res






        
        
        