# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def dfs(self, root, result):
#        if not root:
#            return
#
#        if result['target_sum'] == 0 and result['is_end']:
#            return
#        else:
#            tmp_target_sum = result['target_sum'] - root.val
#            if tmp_target_sum == 0 and not (root.left or root.right):
#                # goal
#                result['target_sum'] = tmp_target_sum
#                result['is_end'] = True
#            else:
#                result['target_sum'] = tmp_target_sum
#                self.dfs(root=root.left, result=result)
#                if result['is_end']:
#                    return
#                self.dfs(root=root.right, result=result)
#                if not result['is_end']:
#                    result['target_sum'] += root.val
#
#    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#        if not root:
#            return False
#        result = {
#            'is_end': False,
#            'target_sum': targetSum
#        }
#        self.dfs(root=root, result=result)
#        return result['is_end']

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val
        ans = self.hasPathSum(root=root.left, targetSum=targetSum)
        if not ans:
            ans = self.hasPathSum(root=root.right, targetSum=targetSum)
        return ans

