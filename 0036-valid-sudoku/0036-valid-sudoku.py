class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        squares = defaultdict(list)
        for r in range(9): 
            for c in range(9): 
                if board[r][c] == '.': 
                    continue
                if (board[r][c] in cols[c] or  board[r][c] in rows[r] or board[r][c] in squares[(r//3, c//3)]) : 
                    return False



                cols[c].append(board[r][c])
                rows[r].append(board[r][c])
                squares[(r//3, c//3)].append(board[r][c])      
        return True