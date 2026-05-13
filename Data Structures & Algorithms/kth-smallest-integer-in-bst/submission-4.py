# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createNodeList(self, node: Optional[TreeNode], nodeList):
        if node.left and self.createNodeList(node.left, nodeList):
            nodeList.append(self.createNodeList(node.left, nodeList))
        if node:
            nodeList.append(node.val)
        if node.right and self.createNodeList(node.right, nodeList):
            nodeList.append(self.createNodeList(node.right, nodeList))
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Find height O(n)
        nodeList = []
        self.createNodeList(root, nodeList)
        return nodeList[k-1]


        