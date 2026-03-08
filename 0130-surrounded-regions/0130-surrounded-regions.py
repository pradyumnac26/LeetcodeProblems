class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c) : 
            board[r][c] = "T"
            for dr, dc in directions : 
                new_r, new_c = r + dr, c+ dc

                if 0<=new_r<len(board) and 0<=new_c<len(board[0]) and board[new_r][new_c] == "O" : 
                    dfs(new_r, new_c)


        for i in range(len(board)): 
            if board[i][0] == "O" : 
                dfs(i, 0)
            if board[i][len(board[0])-1] == "O" : 
                dfs(i, len(board[0])-1) 
        for j in range(len(board[0])): 
            if board[0][j] == "O" : 
                dfs(0, j)
            if board[len(board)-1][j] == "O" :  
                dfs(len(board)-1, j)
        
        for i in range(len(board)): 
            for j in range(len(board[0])) : 
                if board[i][j] == "O" : 
                    board[i][j] = "X"

                if board[i][j] == "T" : 
                    board[i][j] = "O"
        

                


        