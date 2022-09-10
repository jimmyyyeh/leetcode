# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    邏輯與 105. Construct Binary Tree from Preorder and Inorder Traversal 相同, 只是順序上會先取右樹再取左樹
    """
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    #     if not (postorder and inorder):
    #         return
    #     node = TreeNode(val=postorder.pop())
    #
    #     index = inorder.index(node.val)
    #     node.right = self.buildTree(postorder=postorder, inorder=inorder[index + 1:])
    #     node.left = self.buildTree(postorder=postorder, inorder=inorder[:index])
    #     return node

    def construct(self, low, high, postorder, index_map):
        if (low > high) or not postorder:
            return None
        node = TreeNode(val=postorder.pop())
        index = index_map[node.val]
        node.right = self.construct(low=index + 1, high=high, postorder=postorder, index_map=index_map)
        node.left = self.construct(low=low, high=index - 1, postorder=postorder, index_map=index_map)
        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {v: k for k, v in enumerate(inorder)}
        return self.construct(low=0, high=len(inorder) - 1, postorder=postorder, index_map=index_map)
