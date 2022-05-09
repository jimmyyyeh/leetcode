class Solution:
    """
    兩種解題思路:
    1. 組合
        以題目[m, n]為例, 機器人只會向右/下, 向下走(m-1),向右走(n-1),
        而總共會走(m-1)+(n-1)步, 因此我們只要在總和步數(m-1+n-1)取向下走步數(m-1)剩下即為向右走步數(n-1), 反之亦然,
        組合公式為: C(m+n-2)取(m-1)or(n-1)
    2. 動態規劃
        每一個格子為上面的格子往下走 or 左邊的格子往右走,
        因此每個格子的走法為左邊格子的走法數量+上面格子的走法數量,
        邊境條件為四個邊, 只有一種走法
    """
    def uniquePaths(self, m: int, n: int) -> int:
        m_ = (m - 1) + (n - 1)
        n_ = max(m - 1, n - 1)

        denominator = numerator = 1
        for d, n in enumerate(range(m_, n_, -1)):
            numerator *= n
            denominator *= (d + 1)
        return numerator // denominator

        # dp = [[0] * n for _ in range(m)]
        #
        # for i in range(m):
        #     for j in range(n):
        #         if 0 in {i, j}:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]
