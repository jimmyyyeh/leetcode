class Solution:
    @staticmethod
    def reverse_group(head, k):
        """
        反轉前n個元素並回傳
        """
        origin_head = head
        tmp = None
        for i in range(k):
            if not tmp:
                tmp = ListNode(head.val, None)
            else:
                tmp = ListNode(head.val, tmp)
            head = head.next
            if not head and i != k - 1:
                # 若走完但這組無法完整分組(整除), 則不反轉
                return head, origin_head
        return head, tmp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode(None)
        dummy = ans

        while head:
            head, reversed_ = self.reverse_group(head=head, k=k)
            ans.next = reversed_
            while ans.next:
                # 走到最後一個節點, 把反轉後的部分串接上去
                ans = ans.next
        return dummy.next
