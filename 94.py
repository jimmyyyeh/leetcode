# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    兩種解題思路:
    1. 遞迴
    2. 依序迭代節點, 參考下解:
    https://www.youtube.com/watch?v=g_S5WuasWUE
    """

    # def dfs(self, root, result):
    #     if not root:
    #         return
    #     self.dfs(root=root.left, result=result)
    #     result.append(root.val)
    #     self.dfs(root=root.right, result=result)
    #
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = list()
    #     self.dfs(root=root, result=result)
    #     return result
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        stack = list()
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result
