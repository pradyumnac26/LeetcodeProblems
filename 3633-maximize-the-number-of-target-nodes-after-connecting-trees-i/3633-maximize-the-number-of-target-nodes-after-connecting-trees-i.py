class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def adj(e, size):
            mat = [[] for _ in range(size)]
            for src, dest in e:
                mat[src].append(dest)
                mat[dest].append(src)
            return mat

        def bfs(g, start, lim):
            hash = set()
            dq = deque([(start, 0)])
            hash.add(start)
            while dq:
                node, dist = dq.popleft()
                if dist == lim:
                    continue
                for v in g[node]:
                    if v not in hash:
                        hash.add(v)
                        dq.append((v, dist + 1))
            return hash

        n, m = len(edges1) + 1, len(edges2) + 1
        a1 = adj(edges1, n)
        a2 = adj(edges2, m)

        reachableI = [bfs(a1, i, k) for i in range(n)]
        reachableJ = [bfs(a2, j, k - 1) if k > 0 else set() for j in range(m)]

        nodes = [0] * n
        for i in range(n):
            mxCnt = 0
            for j in range(m):
                cnt = len(reachableI[i]) + len(reachableJ[j])
                mxCnt = max(mxCnt, cnt)
            nodes[i] = mxCnt

        return nodes