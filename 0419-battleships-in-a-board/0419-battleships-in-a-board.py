class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1)]
        def dfs(r, c):
            board[r][c] = 'O'
            for dr, dc in directions : 
                new_row, new_col = r + dr, c + dc 
                if 0<=new_row<ROWS and 0<=new_col<COLS and board[new_row][new_col] == 'X': 
                    dfs(new_row, new_col)
  

        battles = 0 
        for i in range(ROWS): 
            for j in range(COLS): 
                if board[i][j] == 'X': 
                    dfs(i, j)
                    battles += 1
        return battles
        