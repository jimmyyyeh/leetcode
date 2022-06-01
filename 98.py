# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    兩種解題思路:
    1. 利用二元樹中序搜尋之結果為排序特性
    2. 定義出每個節點的範圍(floor, ceiling), 去做比較
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

    # def bfs(self, root, floor, ceiling):
    #     if not root:
    #         return True
    #     if not floor < root.val < ceiling:
    #         return False
    #     return self.bfs(root=root.left, floor=floor, ceiling=root.val) and \
    #            self.bfs(root=root.right, floor=root.val, ceiling=ceiling)
    #
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     return self.bfs(root=root, floor=-2 ** 31 - 1, ceiling=2 ** 31)
