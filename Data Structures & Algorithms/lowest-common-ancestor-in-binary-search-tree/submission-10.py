# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(root.left and root.right):
            leftVal = root.left.val
            rightVal = root.right.val
        # Case 1 - Left or Right child doesn't exist then lca is the root
        else: 
            return root

        # Case 2 - P and q correspond to both left or right vals
        if (leftVal == p.val and rightVal == q.val) or (leftVal == q.val and rightVal == p.val):
            return root
        # Case 3 - P or q is root
        elif(root.val == p.val or root.val == q.val):
            return root
        # Case 4 - both p and q are less than the current val 
        if p.val < root.val and q.val < root.val:
            lca = self.lowestCommonAncestor(root.left, p, q)
        # Case 5 - both p andq are greater than the current val
        elif p.val > root.val and q.val > root.val:
            lca = self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        return lca
        


        
