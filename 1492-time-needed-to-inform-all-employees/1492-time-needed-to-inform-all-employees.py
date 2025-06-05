class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(len(manager)):
            adj[manager[i]].append(i)
        q = deque([])
        q.append((headID, 0))
        res = 0  # initial node or manager and time
        while q : 
            node, time = q.popleft()
            res = max(res, time)
            for nei in adj[node]: 
                q.append((nei, time+informTime[node]))
        return res
    

        