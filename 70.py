import math


class Solution:
    """
    兩種解題思路:
    1. 組合
    2. 動態規劃
        n = 1 -> 1
        n = 2 -> 2
        n = 3 -> 最後一階只能選擇由(n-1)走一步 or (n-2)走兩步兩種走法, 因此 = (n-1) + (n-2)
        以此類推
    """

    def climbStairs(self, n: int) -> int:
        # max_two_steps = n // 2  # 計算總步數最多可以容納幾個2步
        # ans = 0
        # for i in range(max_two_steps + 1):
        #     two_steps = i  # 走2步
        #     one_steps = n - 2 * i  # 走1步
        #     # C (one_steps + two_steps) 取 min(one_steps, two_steps), 進行組合
        #     total = one_steps + two_steps
        #     choice = min(one_steps, two_steps)
        #     combination = math.factorial(total) / (math.factorial(choice) * math.factorial(total - choice))
        #     ans += int(combination)
        # return ans
        dp = [1, 2]
        if n <= 2:
            return dp[n-1]

        for _ in range(n - 2):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
