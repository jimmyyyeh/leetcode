# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def list_2_bst(self, nums):
        if not nums:
            return None
        len_ = len(nums)
        index = int(len_ / 2)
        node = TreeNode(val=nums[index])
        node.left = self.list_2_bst(nums=nums[:index])
        node.right = self.list_2_bst(nums=nums[index + 1:])
        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = list()
        while head:
            nums.append(head.val)
            head = head.next
        return self.list_2_bst(nums=nums)
