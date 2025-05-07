from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        # Special case: if all entries in moveTime are 0, return the direct path length
        if all(moveTime[i][j] == 0 for i in range(n) for j in range(m)):
            return n + m - 2  # Direct path from (0,0) to (n-1,m-1)

        # Priority queue (min-heap) to store (time, x, y)
        pq = [(0, 0, 0)]  # Start from the top-left corner at time 0
        
        # 2D list to store the minimum time to reach each cell
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0
        
        # Directions array for moving right, down, left, and up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            current_time, x, y = heapq.heappop(pq)

            # If we reach the bottom-right corner, return the result with +1 for the final move
            if x == n - 1 and y == m - 1:
                return current_time + 1

            # Explore adjacent cells
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                # Check if the new cell is within the grid bounds
                if 0 <= new_x < n and 0 <= new_y < m:
                    arrival_time = current_time + 1
                    
                    # If arrival time is too early, wait until moveTime allows entry
                    if arrival_time < moveTime[new_x][new_y]:
                        arrival_time = moveTime[new_x][new_y]
                    
                    # Update if this path to the cell is shorter than previously recorded
                    if arrival_time < visited[new_x][new_y]:
                        visited[new_x][new_y] = arrival_time
                        heapq.heappush(pq, (arrival_time, new_x, new_y))

        return -1