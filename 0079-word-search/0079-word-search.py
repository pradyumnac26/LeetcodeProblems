class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, i) : 
            if i == len(word) : 
                return True 
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or word[i]!=board[r][c] or (r, c) in path : 
                return False 
            path.add((r, c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
            path.remove((r, c))
            return res
            
            
        path = set()
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if word[0] == board[i][j] and dfs(i,  j  ,0 ) : 
                    return True 
        return False 
        