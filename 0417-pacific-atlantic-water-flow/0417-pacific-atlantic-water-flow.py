class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, prev, vis) : 
            if r < 0 or r >= rows or c < 0 or c >= cols : 
                return 
            if (r, c) in vis : 
                return
            if heights[r][c] <  prev : 
                return 
            
            prev = heights[r][c]
            vis.add((r, c))
            dfs(r+1, c, prev, vis)
            dfs(r, c-1, prev, vis)
            dfs(r-1, c, prev, vis)
            dfs(r, c+1, prev, vis)  


        pac = set()
        atl = set()
        prev = 0
        for c in range(cols) : 
            dfs(0, c, prev, pac)
            dfs(rows-1, c, prev, atl)
        
        for r in range(rows) : 
            dfs(r, 0, prev, pac)
            dfs(r ,cols-1, prev, atl)
        print(pac)
        print(atl)
        res = []
        for r, c in pac : 
            if (r, c) in atl : 
                res.append(list((r,c)))
        return res



        
        