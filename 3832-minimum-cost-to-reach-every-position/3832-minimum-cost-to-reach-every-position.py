class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        m = cost[0]
        res = []
        for i in range(len(cost)):
            m = min(cost[i], m)
            res.append(m)
        return res