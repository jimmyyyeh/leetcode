# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        len_ = len(nums)
        index = int(len_ / 2)
        node = TreeNode(val=nums[index])
        node.left = self.sortedArrayToBST(nums=nums[:index])
        node.right = self.sortedArrayToBST(nums=nums[index + 1:])
        return node
