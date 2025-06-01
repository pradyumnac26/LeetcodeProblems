class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        visit = {}
        
        def dfs(r,c): 
            if r >= m or c >= n : 
                return 0 
            if (r,c) in visit: 
                return visit[(r, c)]
            down = dfs(r+1, c)
            right = dfs(r, c+1)
            diag = dfs(r + 1, c+1)
            if matrix[r][c] == '1' : 
                visit[(r, c)] =  1 + min(down, right, diag)
            else : 
                visit[(r, c)] = 0 
            return visit[(r, c)]

        maxarea = 0
        for i in range(m): 
            for j in range(n): 
                maxarea = max(maxarea, dfs(i, j))
        return maxarea*maxarea
        


        

        