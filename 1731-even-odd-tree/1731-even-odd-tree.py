# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # return true if it satisfies the even odd tree, or else return false 
        q = deque([root])
        res = [] 
        level = 0 
        cnt = 0 
        flag = 1
        while q : 
            level = []
            cnt+=1 
            for _ in range(len(q)): 
                root = q.popleft() 
                if (cnt-1) % 2 == 0 and root.val %2 == 0 : 
                    return False 
                if (cnt-1) % 2 != 0 and root.val %2 != 0 : 
                    return False 
                if len(level) > 0 and (cnt-1) % 2 == 0 and level[-1] >= root.val : 
                    return False
                elif len(level) > 0 and (cnt-1)%2 !=0 and level[-1] <= root.val : 
                    return False 
                if len(level) > 0 : 
                    print(cnt-1, level[-1], root.val)
                level.append(root.val)


                if root.left : 
                    q.append(root.left) 
                if root.right : 
                    q.append(root.right)
            res.append(level)
        print(res)
        if flag == 1 : 
            return True 

        
        

        