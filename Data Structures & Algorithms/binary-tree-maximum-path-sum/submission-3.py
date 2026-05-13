# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMax(self, node: Optional[TreeNode], res):
        if node:
            leftPathVal, resLeft = self.findMax(node.left, res)
            rightPathVal, resRight = self.findMax(node.right, res)    
            bothPathVal = leftPathVal+rightPathVal + node.val
            maxSum = max(leftPathVal +node.val, rightPathVal +node.val, node.val)
            res = max(leftPathVal, rightPathVal, bothPathVal, maxSum, resLeft, resRight)
            print("Curr", node.val)
            print("Left", leftPathVal)
            print("Right", rightPathVal)
            print("Both", bothPathVal)
            print("Global", res)
            print("Max sum", maxSum)
            return maxSum, res
        else:
            return -1000000, -1000000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        currMaxSum, res = self.findMax(root, -1000000)
        return res