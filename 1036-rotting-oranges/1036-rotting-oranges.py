from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # Step 2: BFS to rot adjacent fresh oranges
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        minutes = 0
        
        while queue:
            row, col, time = queue.popleft()
            minutes = time  # Update the time at each level
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within bounds and is a fresh orange
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2  # Rot the fresh orange
                    fresh_oranges -= 1  # Decrease count of fresh oranges
                    queue.append((new_row, new_col, time + 1))  # Add to the queue with updated time
        
        # Step 3: Check if all fresh oranges are rotted
        return minutes if fresh_oranges == 0 else -1
