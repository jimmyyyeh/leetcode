# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        previous = ListNode(val=None, next=None)
        dummy = previous

        tmp = head.val
        head = head.next
        count = 1
        
        while head:
            if tmp != head.val:
                if count == 1:
                    previous.next = ListNode(val=tmp, next=None)
                    previous = previous.next
                tmp = head.val
                count = 1
            else:
                count += 1
            head = head.next

        if count == 1:
            previous.next = ListNode(val=tmp, next=None)
            previous = previous.next
        return dummy.next

