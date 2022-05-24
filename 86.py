# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(val=None, next=None)
        right = ListNode(val=None, next=None)
        left_dummy = left
        right_dummy = right

        while head:
            if head.val < x:
                left.next = ListNode(val=head.val, next=None)
                left = left.next
            else:
                right.next = ListNode(val=head.val, next=None)
                right = right.next

            head = head.next

        left.next = right_dummy.next
        return left_dummy.next
