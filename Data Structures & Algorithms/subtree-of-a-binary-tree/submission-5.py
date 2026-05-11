# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(subRoot == None and root):
            return True
        if(root == None):
            return False
        elif(self.isSametree(root, subRoot)):
            return True
        elif(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)):
            return True
        else:
            return False

    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p and q):
            if(p.val == q.val):
                return (self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right))
            else:
                return False
        elif(p or q):
            return False
        else:
            return True