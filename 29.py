class Solution:
    """
    利用直式除法的概念, 依序取位數, 範例如下:
    53218 / 13
    -> 起始: 53 剩餘 218
    53 / 13 = 4 ... 1 -> 1 補 2 -> 12
    12 / 13 = 0 ... 12 -> 12 補 1 -> 121
    121 / 13 = 9 ... 4 -> 4 補 8 -> 48
    48 / 13 = 3 ... 9 -> end
    -> ans: 4 0 9 3 (每回合的商數)
    """

    @staticmethod
    def do_divide(dividend, divisor, ans_list):
        ans = 0
        while dividend >= divisor:
            dividend -= divisor
            ans += 1
        ans_list.append(str(ans))
        return dividend

    def divide(self, dividend: int, divisor: int) -> int:
        negative = abs(dividend) + abs(divisor) != abs(divisor + dividend)
        dividend = abs(dividend)
        divisor = abs(divisor)

        divisor_digit = len(str(divisor))
        dividend_list = list(str(dividend))
        dividend = int(''.join(dividend_list[:divisor_digit]))
        dividend_list = dividend_list[divisor_digit:]

        ans_list = []
        while dividend_list:
            dividend = self.do_divide(dividend=dividend, divisor=divisor, ans_list=ans_list)

            next_ = dividend_list.pop(0)
            dividend = int(f'{dividend}{next_}')

        # 取完到最後一位數後還要再做一次
        self.do_divide(dividend=dividend, divisor=divisor, ans_list=ans_list)

        ans = int(''.join(ans_list))
        ans = 0 - ans if negative else ans
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if ans < -2 ** 31:
            return -2 ** 31
        return ans
