# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    解題思路:
    第一個想法是把right節點儲存在stack內, 然後依序將左節點去替換掉右邊的節點, 最後再依序把右邊節點接下去,
    但實作上遇到問題, 因此先採最保守的解法(解法1)
    1. 走訪完所有節點, 再依序替換回去node裏面
    2. 和linked list一樣, 基本上遇到in-place的問題就優先考慮做dummy節點, 結合一開始的思路, 節點儲存在stack FIFO, 依序走訪即可, 參考下解:
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37065/simple-dfs-python-solution
    """

    # def dfs(self, root, values):
    #     if not root:
    #         return
    #     values.append(root.val)
    #     self.dfs(root=root.left, values=values)
    #     self.dfs(root=root.right, values=values)
    #
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if not root:
    #         return
    #
    #     values = list()
    #     self.dfs(root=root, values=values)
    #
    #     for value in values[1:]:
    #         root.left = None
    #         root.right = TreeNode(value)
    #         root = root.right

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            dummy.right = node
            dummy.left = None
            stack.append(node.right)
            stack.append(node.left)
            dummy = node
