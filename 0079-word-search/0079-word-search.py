class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        
        def dfs(r, c, i) : 
            if i == len(word) : 
                return True 
            
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[i]!=board[r][c] or (r, c) in vis : 
                return False 

            vis.add((r, c)) 
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1) 
            vis.remove((r,c))
            return res



        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vis = set()
        i = 0 
        for r in range(len(board)) : 
            for c in range(len(board[0])) : 
                if word[0] == board[r][c] and dfs(r, c, 0) : 
                    return True 
        return False 
        