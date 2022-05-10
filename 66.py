class Solution:
    """
    兩種解題思路:
    1. 從尾巴依序迭代, 確認是否要進位, 如果要則當位數改為0, 繼續往前做, 否則直接更新當前位數
    2. 將list轉為數字, 運算後再轉回list
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        # len_ = len(digits)
        # for index, digit in enumerate(digits[::-1]):
        #     index_ = len_ - index - 1
        #     tmp = digit + 1
        #     if tmp == 10:
        #         digits[index_] = 0
        #         if index_ == 0:
        #             digits = [1] + digits
        #     else:
        #         digits[index_] = tmp
        #         break
        # return digits

        num = ''
        for digit in digits:
            num += str(digit)
        num = int(num)
        num += 1
        return list(str(num))
