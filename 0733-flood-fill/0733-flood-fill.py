class Solution:
    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # Base Case: If the starting pixel already has the target color
        if original_color == color:
            return image
        
        def dfs(r, c):
            # Check boundaries and ensure the pixel has the original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            # Change the color
            image[r][c] = color
            
            # Move in 4 directions: up, down, left, right
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Start DFS from the given starting pixel
        dfs(sr, sc)
        return image
