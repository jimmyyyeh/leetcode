# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, path, depth_list, root):
        if not root:
            return
        else:
            path.append(root.val)
            if not (root.left or root.right):
                depth = len(path.copy())
                depth_list.append(depth)
            else:
                self.dfs(path=path, depth_list=depth_list, root=root.left)
                self.dfs(path=path, depth_list=depth_list, root=root.right)
            path.pop()

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        path = list()
        depth_list = list()
        self.dfs(path=path, depth_list=depth_list, root=root)
        return min(depth_list)

