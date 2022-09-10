# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return root
        #
        # level_dict = {}
        # stack = [{'level': 0, 'node': root}]
        #
        # while stack:
        #     root = stack.pop()
        #     node, level = root['node'], root['level']
        #
        #     level_dict.setdefault(level, list())
        #
        #     level_dict[level].append(node.val)
        #
        #     if node.right:
        #         stack.append({'level': level + 1, 'node': node.right})
        #     if node.left:
        #         stack.append({'level': level + 1, 'node': node.left})
        #
        # return list(level_dict.values())

        results = list()
        queue = list()
        queue.append(root)

        while queue:
            level = []
            level_len = len(queue)
            # cache住當前層級的長度, 新append進去的都是下一層級的node
            for _ in range(level_len):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                results.append(level)

        return results
