class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = defaultdict(list)
        for i,n in enumerate(edges): 
            adj[i].append(n)
        

        def bfs(src, distMap): 
            q = deque([(src, 0)])
            while q: 

                node, dist = q.popleft()
                distMap[node] = dist
                for nei in adj[node]: 
                    if nei not in distMap: 
                        q.append((nei, dist+1))



        hmap1 = {} 
        hmap2 = {} 
        bfs(node1, hmap1)
        bfs(node2, hmap2 )

        res = -1 
        resDist = float('inf')
        for i in range(len(edges)): 
            if i in hmap1 and i in hmap2: 
                dist = max(hmap1[i], hmap2[i])
                if dist < resDist : 
                    res = i
                    resDist = dist
        return res

        