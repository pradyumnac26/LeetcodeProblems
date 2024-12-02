class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        if col == n:
            ans.append([''.join(row) for row in board])  # Convert board to a list of strings
            return

        for row in range(n):
            if leftrow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
                board[row][col] = 'Q'  # Place queen
                leftrow[row] = 1  # Mark row as used
                lowerDiagonal[row + col] = 1  # Mark lower diagonal as used
                upperDiagonal[n - 1 + col - row] = 1  # Mark upper diagonal as used

                self.solve(col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)

                # Backtrack
                board[row][col] = '.'
                leftrow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]  # Initialize the board with empty spaces
        leftrow = [0] * n  # Tracks usage of rows
        upperDiagonal = [0] * (2 * n - 1)  # Tracks usage of upper diagonals
        lowerDiagonal = [0] * (2 * n - 1)  # Tracks usage of lower diagonals

        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans


