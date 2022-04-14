# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    範例如: 1 2 3 4 5 6
    第一步驟會變成:
          2       |       1       |       3 4 5 6
    head.next.val      head.val        head.next.next
    完成第一次移動後, 再從head.next.next開始重複動作, 因此同時移動pointer跟head兩位, 依此類推
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = ListNode(None)
        dummy = pointer
        if not head:
            return None

        if not head.next:
            return head

        while True:
            if not head.next:
                # 奇數的情形 最後一位直接跳過
                break
            val_ = head.val
            next_val = head.next.val
            pointer.next = head.next
            pointer.next.val = val_
            pointer.val = next_val
            pointer = head.next.next
            head = head.next.next
            if not head:
                break
        return dummy
