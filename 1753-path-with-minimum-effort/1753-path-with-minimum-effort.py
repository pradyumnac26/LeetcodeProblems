from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        effort = [[float('inf')] * n for _ in range(m)]
        effort[0][0] = 0
        min_heap = [(0, 0, 0)] 

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while min_heap:
            curr_effort, x, y = heappop(min_heap)
            if (x, y) == (m-1, n-1):
                return curr_effort 

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    diff = abs(heights[nx][ny] - heights[x][y])
                    max_effort = max(curr_effort, diff)
                    if max_effort < effort[nx][ny]:
                        effort[nx][ny] = max_effort
                        heappush(min_heap, (max_effort, nx, ny))

        return -1  # Should never reach here
