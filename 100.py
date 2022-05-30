# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = list()
        q_stack = list()

        while (p and q) or (p_stack and q_stack):
            while p and q:
                if p.val != q.val:
                    # 當前節點不同
                    return False
                p_stack.append(p)
                q_stack.append(q)
                p = p.left
                q = q.left
            if p != q:
                # 表示當其中一為None時, 而另一節點還可以繼續走訪
                return False
            p = p_stack.pop()
            q = q_stack.pop()
            p = p.right
            q = q.right
        return p == q
