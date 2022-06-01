# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    利用二元樹中序搜尋之結果為排序特性
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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

        for index, num in enumerate(result[:-1]):
            if num >= result[index + 1]:
                return False
        return True
