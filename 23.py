# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    題目已經排序所有的ListNode, 所以依序比較第一個元素, 最小的就取出
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if all(not list_ for list_ in lists):
            return None
        pointer = ListNode(None)
        dummy = pointer
        while True:
            tmp = 10 ** 4 + 1  # 題目有給限制
            selected_index = 0
            for index, list_ in enumerate(lists):
                if list_ and list_.val < tmp:
                    tmp = list_.val
                    selected_index = index
            pointer.next = lists[selected_index]
            lists[selected_index] = lists[selected_index].next
            pointer = pointer.next
            if lists.count(None) == len(lists):
                break
        return dummy.next
