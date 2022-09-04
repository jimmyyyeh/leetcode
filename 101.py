# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def check_left_equals_to_right(self, left, right):
        if not left and not right:
            # 最終的節點
            return True
        elif not (left and right):
            # 缺左邊or缺右邊
            return False
        else:
            if left.val != right.val:
                ans = False
            else:
                # 要檢查左樹=右樹
                ans = self.check_left_equals_to_right(left=left.left, right=right.right)
                if ans:
                    ans = self.check_left_equals_to_right(left=left.right, right=right.left)
            return ans

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_left_equals_to_right(left=root.left, right=root.right)
