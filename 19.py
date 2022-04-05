# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        TODO
        兩種解題思路:
        1. 取得總長度, 用正數的方式移除
        2. 快慢指針, 先將快指針走n步, 接著一起走, 當快指針走到底時, 慢指針會停在要移除節點的前一點
        """
        # values = list()
        # while head:
        #     values.append(head.val)
        #     head = head.next
        #
        # ans = None
        # for index, value in enumerate(values[::-1]):
        #     if index == n - 1:
        #         continue
        #     if not ans:
        #         ans = ListNode(val=value, next=None)
        #     else:
        #         ans = ListNode(val=value, next=ans)
        # return ans
        fast = ListNode(val=0, next=head)
        slow = ListNode(val=0, next=head)
        move = 0
        while fast.next.next:
            move += 1
            fast.next = fast.next.next
            if move > n:
                slow.next = slow.next.next

        if n - move == 1:
            # 移除頭一個節點
            return head.next
        else:
            slow.next.next = slow.next.next.next
            return head
