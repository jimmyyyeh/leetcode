# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    TODO
    以[1, 2, 3, 4, 5]來看, 假設選擇3, [1, 2]一定在左邊的子樹, [4, 5]一定在右邊的子樹 -> [1, 2] 3 [4, 5]
    [1, 2] -> [], 1, [2] ...
    [3, 4] -> [], 3, [4] ...
    去做遞迴, 再依序append根節點
    """

    def dfs(self, nums, cache):
        if not nums:
            return 1
        key = (nums[0], nums[-1])
        if key in cache:
            return cache[key]
        count = 0
        for index, num in enumerate(nums):
            left_trees = self.dfs(nums=nums[:index], cache=cache)
            right_trees = self.dfs(nums=nums[index + 1:], cache=cache)
            count += left_trees * right_trees
        cache[key] = count
        return count

    def numTrees(self, n: int) -> int:
        return self.dfs(nums=list(range(1, n + 1)), cache=dict())
