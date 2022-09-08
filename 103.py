# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        level_dict = {}
        stack = [{'level': 0, 'node': root}]
        while stack:
            root = stack.pop()
            node, level = root['node'], root['level']

            level_dict.setdefault(level, list())
            if level % 2 == 0:
                level_dict[level].append(node.val)
            else:
                level_dict[level] = [node.val] + level_dict[level]

            if node.right:
                stack.append({'level': level + 1, 'node': node.right})
            if node.left:
                stack.append({'level': level + 1, 'node': node.left})

        return list(level_dict.values())
