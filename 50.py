class Solution:
    """
    兩種解題思路:
    1. 處理完特殊狀況, 照著乘法的邏輯去做
    2. 將指數/2去做遞迴, 直到剩下1(不可除)為止
    """
    # def myPow(self, x: float, n: int) -> float:
    #     if x in {0, 1}:
    #         return x
    #     elif x == -1:
    #         return -1 if n % 2 != 0 else 1
    #
    #     is_reciprocal = n < 0
    #     x = 1 / x if is_reciprocal else x
    #     ans = 1
    #     for _ in range(abs(n)):
    #         ans *= x
    #         if ans == 0 or not -10000 <= ans <= 10000:
    #             return 0
    #     return ans

    def calculate(self, x, n):
        if n == 1:
            return x
        result = self.calculate(x=x, n=n // 2)
        ans = result * result
        return ans if n % 2 == 0 else ans * x

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            return self.calculate(x=x, n=n) if n > 0 else self.calculate(x=1 / x, n=-n)
