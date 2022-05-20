# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = ListNode(val=None, next=None)
        dummy = previous
        while head:
            if previous.val != head.val:
                previous.next = ListNode(val=head.val, next=None)
                previous = previous.next
            head = head.next
        return dummy.next
