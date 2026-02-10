# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # depth of the 2 subtree (left and right) starting at any node of the tree, should not differ by more than 1.  
        # and should return a tree with that node as the start 
        # so i need to try starting every node as the root, and its tree to see if its 2 substrees heoghts differ. 
        # so its like the tree ha to be skewed for us to find a subtree which can be transformed into another tree with teh given conditions.. 
        # because if i already have a cmomplet binary tree then it by itself is a balanced binary tree right.. 
        # so lets consider an example ... 
        #             7
        #         3       9.   =>> this also inorder traverasal would be 1, 2, 3, 7, 9 ==> consider a mid element, construct and return ?? 
        #     2               
        # 1
# so my observatio is lie, whichever side has mode height in the current tree, try one ndode from there, and when u try only the nodes to the left of that would remain in the left, and the nodes above it would remain in the right, so u just need a count of number of nodes above a certain node, and the number of nodes below, to be able to calculate if a balnced tree can be formed, but we will have to return the tree itself as per the qn 
# construct a new tree with every node... 
        res = []
        def inorder(root) : 
            if not root : 
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)


        print(res)
        def build(res) : 
            if not res : 
                return None 
            m = len(res)//2
            node = TreeNode(res[m])
            node.left = build(res[:m])
            node.right = build(res[m+1:])
            return node

        inorder(root)
        return build(res)




        






        