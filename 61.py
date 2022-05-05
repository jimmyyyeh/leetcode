# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    k會以ListNode的長度為一循環, 因此求餘數即可表k,
    如範例head = [1, 2, 3, 4, 5], k = 2 -> [4, 5, 1, 2, 3],
    視同把head分成 [1, 2, 3] [4, 5], 接著把[1, 2, 3]接到[4, 5]的尾
    1. 先求出總數, 簡化k的數量
    2. 緩存目前所需要的前段ListNode
    3. 遍歷剩下的ListNode走到最一個元素後, 接上
    """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not k:
            return head

        walker = ListNode()
        walker.next = head

        count = 0
        while walker:
            walker = walker.next
            count += 1
        count -= 1  # 前面是從0開始, 因此要-1

        k %= count  # 求餘數
        k = count - k  # 扣掉後才是前段需要緩存的ListNode

        tmp = ListNode(val=0, next=None)
        dummy = tmp
        for _ in range(k):
            tmp.next = ListNode(val=head.val)
            head = head.next
            tmp = tmp.next

        if not head:
            return dummy.next

        walker = head
        while walker.next:
            walker = walker.next
        walker.next = dummy.next
        return head
