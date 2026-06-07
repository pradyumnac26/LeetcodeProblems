# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        # a node that has no parent would be the main root. 
        # every node in the tree is a tree node. 
        tree = [] 
        nodes = {} 
        s = set() 
        for p, c, isLeft in descriptions : 
            if p not in nodes : 
                nodes[p] = TreeNode(p) 
            if c not in nodes : 
                nodes[c] = TreeNode(c)
            

            if isLeft : 
                nodes[p].left = nodes[c]
            else : 
                nodes[p].right = nodes[c]
            s.add(c) 

        
        for x in nodes : 
            if x not in s : 
                return nodes[x]
            






        