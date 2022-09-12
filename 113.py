# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, path, path_list, root, target_sum):
        if not root:
            return
        else:
            path.append(root.val)
            if not (root.left or root.right):
                sum_ = sum(path.copy())
                if sum_ == target_sum:
                    path_list.append(path.copy())
            else:
                self.dfs(path=path, path_list=path_list, root=root.left, target_sum=target_sum)
                self.dfs(path=path, path_list=path_list, root=root.right, target_sum=target_sum)
            path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        path = list()
        path_list = list()
        self.dfs(path=path, path_list=path_list, root=root, target_sum=targetSum)
        return path_list

