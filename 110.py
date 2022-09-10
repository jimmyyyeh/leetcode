# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_level(self, root):
        if root is None:
            return 0
        left = self.get_level(root=root.left)
        right = self.get_level(root=root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            # -1代表不平衡, 左右子樹皆為平衡, 且兩子樹的深度差不可大於1
            return -1
        return 1 + max(left, right)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.get_level(root=root) != -1
