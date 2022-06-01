# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    兩種解題思路:
    1. 先透過中序法遍歷, 當遇到一個新元素時, current必定大於previous,
       因此在中間如果遇到previous>current, 則將元素依序往前作交換(類似泡沫排序)
    2. 先將數字全部讀取出來之後排序, 接著update回每一個非None的節點
    """

    # def recoverTree(self, root: Optional[TreeNode]) -> None:
    #     results = list()
    #     stack = list()
    #     current = root
    #     previous = 2 ** 31
    #     while current or stack:
    #         while current:
    #             stack.append(current)
    #             current = current.left
    #         current = stack.pop()
    #         if previous and current.val < previous:
    #             for result in results:
    #                 if current.val < result.val:
    #                     result.val, current.val = current.val, result.val
    #         results.append(current)
    #         previous = current.val
    #         current = current.right
    #     return root

    def dfs(self, root, nodes):
        if not root:
            return
        self.dfs(root=root.left, nodes=nodes)
        nodes.append(root)
        self.dfs(root=root.right, nodes=nodes)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nodes = list()
        self.dfs(root=root, nodes=nodes)
        values = sorted([node.val for node in nodes])

        for index, value in enumerate(sorted(values)):
            nodes[index].val = value
        return root
