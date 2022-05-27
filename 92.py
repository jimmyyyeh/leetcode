# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        left_node = ListNode(val=None, next=None)
        left_dummy = left_node
        right_node = ListNode(val=None, next=None)
        right_dummy = right_node
        reversed_val = list()

        index = 1
        while head:
            if left <= index <= right:
                reversed_val.append(head.val)
            elif index < left:
                left_node.next = ListNode(val=head.val, next=None)
                left_node = left_node.next
            else:
                right_node.next = ListNode(val=head.val, next=None)
                right_node = right_node.next
            index += 1
            head = head.next

        for val in reversed_val[::-1]:
            left_node.next = ListNode(val=val, next=None)
            left_node = left_node.next
        left_node.next = right_dummy.next

        return left_dummy.next
