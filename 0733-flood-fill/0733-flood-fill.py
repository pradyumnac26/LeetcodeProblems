class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if image[sr][sc] == color:
            return image
        def dfs(r, c, original) : 
            image[r][c] = color 
            for dr, dc in directions : 
                new_r, new_c = r + dr, c + dc 
                if 0<=new_r<len(image) and 0<=new_c < len(image[0]) and image[new_r][new_c] == original : 
                    dfs(new_r, new_c, original)



        dfs(sr, sc, image[sr][sc])
        return image



    
        