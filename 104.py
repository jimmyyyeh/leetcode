# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_level = 1
        stack = [{'level': 1, 'node': root}]
        while stack:
            node = stack.pop()
            level, node = node['level'], node['node']
            max_level = level if level > max_level else max_level

            if node.left:
                stack.append({'level': level + 1, 'node': node.left})
            if node.right:
                stack.append({'level': level + 1, 'node': node.right})

        return max_level
