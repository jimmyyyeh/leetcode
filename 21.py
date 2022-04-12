# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        tmp = list()
        while list1 and list2:
            if not list1 or list1.val > list2.val:
                tmp.append(list2.val)
                list2 = list2.next
            else:
                tmp.append(list1.val)
                list1 = list1.next
        while list1:
            tmp.append(list1.val)
            list1 = list1.next
        while list2:
            tmp.append(list2.val)
            list2 = list2.next

        ans = ListNode(val=tmp[-1])
        for i in tmp[:-1][::-1]:
            ans = ListNode(val=i, next=ans)
        return ans
