class Solution:
    """
    兩種解題思路:
    1. 十分逼近法
    2. 二分法
    """

    def mySqrt(self, x: int) -> int:
        # previous = 0
        # for i in range(0, 46341 + 1):
        #     if x == i * i:
        #         return i
        #     elif previous * previous < x < i * i:
        #         return previous
        #     else:
        #         previous = i

        left, right = 0, x
        while left + 1 < right:
            input([left, right])
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid
        # 因題目要求回傳整數部分, 如3.11111 ~ 4 之間都是回傳3
        return right if right * right == x else left
