class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # multisource bfs
        ROWS, COLS = len(mat), len(mat[0])
        vis = [[0]*COLS for _ in range(ROWS)]
        dist = [[0]*COLS for _ in range(ROWS)]
        q = deque()
        for i in range(len(mat)): 
            for j in range(COLS): 
                if mat[i][j] == 0 : 
                    q.append((i, j))
                    vis[i][j] = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q : 
            r, c= q.popleft()
            for dr, dc in directions: 
                new_row, new_col = r + dr, c + dc 
                if 0<=new_row<ROWS and 0<=new_col<COLS and vis[new_row][new_col]==0 and mat[new_row][new_col] == 1 :
                    q.append((new_row, new_col)) 
                    dist[new_row][new_col] = 1 + dist[r][c]
                    vis[new_row][new_col] = 1
        return dist




        
        
        