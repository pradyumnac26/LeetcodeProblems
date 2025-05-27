class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')]*n
        dist[k-1] = 0
        for i in range(n-1): 
            for u, v, wt in times : 
                if dist[u-1] + wt < dist[v-1]:
                    dist[v-1] = dist[u-1]+wt
        max_dist = max(dist)
        return max_dist if max_dist < float('inf') else -1
        