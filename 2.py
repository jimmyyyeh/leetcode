# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    @staticmethod
    def node2str(list_node):
        val_ = list_node.val
        next_ = getattr(list_node, 'next')
        str_ = f'{val_}'
        while True:
            if next_:
                val_ = next_.val
                str_ = f'{val_}{str_}'
                next_ = getattr(next_, 'next')
            else:
                break
        return str_
    
    @staticmethod
    def str2node(str_):
        node = None
        for index in range(len(str_)):
            val = str_[index]
            node = ListNode(val=val, next=node)
        return node
                
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = self.node2str(l1)
        l2_str = self.node2str(l2)
        sum_ = str(int(l1_str) + int(l2_str))
        ans = self.str2node(str_=sum_)
        return ans

