# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.levelDict = {}
    def recursion(self, node, level):
        level += 1
        if node.left:
            l = self.recursion(node.left, level)
        if node.right:    
            r = self.recursion(node.right, level)
        self.levelDict.setdefault(level, []).append(node.val)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            self.recursion(root, -1)
        output = [self.levelDict[i] for i in range(len(self.levelDict))]
        return output
