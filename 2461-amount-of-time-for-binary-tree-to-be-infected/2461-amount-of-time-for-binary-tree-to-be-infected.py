# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        def buildGraph(node, parent):
            if not node : 
                return 
            if parent : 
                adj[node.val].append(parent.val)
                adj[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root, None)

        q = deque([(start, 0)])
        visited = set()
        visited.add(start)
        while q : 
            curr, time = q.popleft()
            final = time
            for nei in adj[curr] : 
                if nei not in visited : 
                    visited.add(nei)
                    q.append((nei, time+1))
        return final




        