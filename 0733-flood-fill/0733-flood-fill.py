class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init = image[sr][sc] 
        if init == color : 
            return image
        def dfs(r, c) : 
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) : 
                return
            if image[r][c] != init : 
                return
            if image[r][c] == init : 
                image[r][c] = color

            
            
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c )
            dfs(r, c-1)




        dfs(sr, sc)  
        return image

        


        
        