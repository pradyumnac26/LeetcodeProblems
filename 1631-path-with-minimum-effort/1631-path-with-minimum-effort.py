class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        minHeap = [(0, 0, 0)] # effort, r, c 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        effort = [[float("inf")]*len(heights[0]) for _ in range(len(heights))]
        effort[0][0] = 0
        n = len(heights) 
        m = len(heights[0])

        while minHeap : 
            curreffort, r, c = heapq.heappop(minHeap)
            for dr, dc in directions : 
                new_r, new_c = r + dr, c + dc 
                if 0<=new_r<len(heights) and 0<=new_c<len(heights[0]) : 
                    edge = abs(heights[new_r][new_c] - heights[r][c]) 
                    neweffort = max(edge, curreffort)
                    if neweffort < effort[new_r][new_c]: 
                        effort[new_r][new_c] = neweffort
                        heapq.heappush(minHeap, (neweffort, new_r, new_c)) 
        return effort[n-1][m-1]
  





        