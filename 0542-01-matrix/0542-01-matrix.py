class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[0]*cols for _ in range(rows)]
        q = deque()
        for i in range(rows) : 
            for j in range(cols) : 
                if mat[i][j] == 0 : 
                    q.append((i, j, 0))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q : 
            r, c, d = q.popleft()
            for dr, dc in directions : 
                new_r, new_c = r + dr, c + dc 
                if 0 <= new_r < rows and 0<=new_c < cols and mat[new_r][new_c] == 1 : 
                    dist[new_r][new_c] = d + 1
                    mat[new_r][new_c] = 0
                    q.append((new_r, new_c, d+1))
        return dist  





        