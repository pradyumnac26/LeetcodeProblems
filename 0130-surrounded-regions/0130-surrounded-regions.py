class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = [[0]*COLS for _ in range(ROWS)]
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c): 
            visited[r][c] = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc] and board[nr][nc] == 'O':
                    dfs(nr, nc)

        for i in range(ROWS): 
            if board[i][0] == 'O' and not visited[i][0]:
                dfs(i, 0)
            if board[i][COLS-1] == 'O' and not visited[i][COLS-1]:
                dfs(i, COLS-1)

        for j in range(COLS): 
            if board[0][j] == 'O' and not visited[0][j]:
                dfs(0, j)
            if board[ROWS-1][j] == 'O' and not visited[ROWS-1][j]:
                dfs(ROWS-1, j)

        for i in range(ROWS):
            for j in range(COLS): 
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'



        