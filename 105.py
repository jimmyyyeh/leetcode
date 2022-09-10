# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    以題目為例, 依序迭代preorder的第一個元素為root, inorder遇到root.val節點的左邊皆為其左子樹, 反之則為右子數
    TODO:
    優化解, 將index存在dict內, 可以降低時間複雜度
    """

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if not (preorder and inorder):
    #         return
    #     node = TreeNode(val=preorder.pop(0))
    #
    #     index = inorder.index(node.val)
    #
    #     node.left = self.buildTree(preorder=preorder, inorder=inorder[:index])
    #     node.right = self.buildTree(preorder=preorder, inorder=inorder[index + 1:])
    #     return node

    def construct(self, low, high, preorder, index_map):
        if (low > high) or not preorder:
            return None
        node = TreeNode(val=preorder.pop(0))
        index = index_map[node.val]
        node.left = self.construct(low=low, high=index - 1, preorder=preorder, index_map=index_map)
        node.right = self.construct(low=index + 1, high=high, preorder=preorder, index_map=index_map)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {v: k for k, v in enumerate(inorder)}
        # low, high去避免多餘的None節點出現
        return self.construct(low=0, high=len(inorder) - 1, preorder=preorder, index_map=index_map)
