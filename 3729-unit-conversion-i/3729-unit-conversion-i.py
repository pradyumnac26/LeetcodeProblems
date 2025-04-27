class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for s,t,c in conversions : 
            adj[s].append((t,c))
        print(adj)

        q = deque([0])
        mod = 10**9 + 7 
        ans = [1]*(len(conversions)+1)
        while q : 
            node = q.popleft()
            for nei in adj[node]: 
                tar, c = nei
                ans[tar] = (ans[node]*c)%mod
                q.append((tar))
        return ans








        