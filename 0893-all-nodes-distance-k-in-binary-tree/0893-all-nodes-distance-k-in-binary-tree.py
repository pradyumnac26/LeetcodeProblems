# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def buildGraph(node, parent): 
            if not node: 
                return 
            if parent : 
                adj[node.val].append(parent.val)
                adj[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root, None)
        q = deque([(target.val, 0)])

        res = []
        visit = set()
        visit.add(target.val)
        while q : 
            curr, dist = q.popleft()
            if dist == k : 
                res.append(curr)
            
            for nei in adj[curr]: 
                if nei not in visit : 
                    visit.add(nei)
                    q.append((nei, dist+1))
        return res 





        