class Solution:
    """
    兩種解題思路:
    1. 延續 Unique Binary Search Trees II 概念, 只需算出所有組合即可
    2. dp:
        [1, 2, 3, 4]
        -> 假設以2為節點 -> [1] 2 [3, 4] -> dp[1] * dp[2](位數)
        -> dp[4] = dp[0] * dp[3] + ([] 1 [2, 3, 4])
                   dp[1] * dp[2] + ([1] 2 [3, 4])
                   dp[2] * dp[1] + ([1, 2] 3 [4])
                   dp[3] * dp[0]   ([1, 2, 3] 4 [])
    """

    # def dfs(self, nums, cache):
    #     if not nums:
    #         return 1
    #     key = (nums[0], nums[-1])
    #     if key in cache:
    #         return cache[key]
    #     count = 0
    #     for index, num in enumerate(nums):
    #         left_trees = self.dfs(nums=nums[:index], cache=cache)
    #         right_trees = self.dfs(nums=nums[index + 1:], cache=cache)
    #         count += left_trees * right_trees
    #     cache[key] = count
    #     return count
    #
    # def numTrees(self, n: int) -> int:
    #     return self.dfs(nums=list(range(1, n + 1)), cache=dict())

    def numTrees(self, n: int) -> int:
        dp = [1, 1]
        for nodes in range(2, n + 1):
            total = 0
            for node in range(1, nodes + 1):
                total += dp[node - 1] * dp[nodes - node]
            dp.append(total)
        return dp[n]

