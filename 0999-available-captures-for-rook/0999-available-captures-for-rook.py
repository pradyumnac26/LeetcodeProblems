class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row, col = -1, -1

        # find the rook
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    row, col = i, j
                    break
            if row != -1:
                break

        captures = 0

        # up
        i = row - 1
        while i >= 0:
            if board[i][col] == "B":
                break
            if board[i][col] == "p":
                captures += 1
                break
            i -= 1

        # down
        i = row + 1
        while i < len(board):
            if board[i][col] == "B":
                break
            if board[i][col] == "p":
                captures += 1
                break
            i += 1

        # left
        j = col - 1
        while j >= 0:
            if board[row][j] == "B":
                break
            if board[row][j] == "p":
                captures += 1
                break
            j -= 1

        # right
        j = col + 1
        while j < len(board[0]):
            if board[row][j] == "B":
                break
            if board[row][j] == "p":
                captures += 1
                break
            j += 1

        return captures