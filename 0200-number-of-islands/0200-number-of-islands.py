class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c) : 
      
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) : 
                return

            if (r, c) in vis : 
                return   

            if grid[r][c] == "0" : 
                return 
            


            vis.add((r, c))
            for dr, dc in directions : 
                new_dr, new_dc = r + dr, c + dc
                if  0<=new_dr<len(grid) and 0<=new_dc<len(grid[0]) and grid[new_dr][new_dc] == "1" : 
                    dfs(new_dr, new_dc)

            
                
        

        cnt = 0 
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        vis = set()
        for i in range(len(grid)): 
            for j in range(len(grid[0])) : 
                if grid[i][j] == "1" and (i, j) not in vis: 
                    dfs(i, j)
                    cnt+= 1
        return cnt 


        