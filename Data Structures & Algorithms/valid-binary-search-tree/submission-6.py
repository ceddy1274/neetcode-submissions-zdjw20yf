# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(float('-inf'), float('inf'), root)
    def isValid(self, minVal, maxVal, root: Optional[TreeNode]) -> bool:
        if root.val <= minVal or root.val >= maxVal:
            return False
        else:
            # Left exists and is less than root
            if(root.left and root.left.val < root.val):
                isLeft = self.isValid(minVal, root.val, root.left)
            # Left exists and is greater than or equal to root
            elif(root.left):
                isLeft = False
            # Left is none
            else:
                isLeft = True

            # Right exists and is less than root
            if(root.right and root.right.val > root.val):
                isRight = self.isValid(root.val, maxVal, root.right)
            # Right exists and is greater than or equal to root
            elif(root.right):
                isRight = False
            # Right is none
            else:
                isRight = True
            
            if(isLeft and isRight):
                return True
            else:
                return False
            
            




















    