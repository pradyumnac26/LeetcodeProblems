from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]  # Initialize the height matrix with -1
        queue = deque()

        # Initialize the queue with all water cells and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))

        # Directions for the 4-adjacent cells (north, east, south, west)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # BFS to propagate heights
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the new cell is within bounds and has not been visited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1  # Increment the height
                    queue.append((nx, ny))  # Add the new cell to the queue

        return height
