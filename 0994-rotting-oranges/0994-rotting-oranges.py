class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        vis = set()
        fresh = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 2 : 
                    q.append((i, j, 0))
                    vis.add((i, j))
                if grid[i][j] == 1 : 
                    fresh+=1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        time = 0 
        while q : 
            r, c, time = q.popleft() 
            for dr, dc in directions : 
                new_r, new_c = r + dr, c + dc 
                if 0<=new_r<len(grid) and 0<=new_c < len(grid[0]) and (new_r, new_c) not in vis and grid[new_r][new_c] == 1 : 
                    vis.add((new_r, new_c))
                    q.append((new_r, new_c, time+1))
                    fresh-=1 
        if fresh : 
            return -1 
        else : 
            return time




        