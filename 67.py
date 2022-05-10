class Solution:
    """
    兩種解題思路:
    1. 迭代數字依序相加, 進位
    2. 將binary轉為int, 相加完再轉回binary
    """
    def addBinary(self, a: str, b: str) -> str:
        # carry = 0
        # result = ''
        # while a or b:
        #     a_ = int(a[-1]) if a else 0
        #     b_ = int(b[-1]) if b else 0
        #     tmp = a_ + b_ + carry
        #     if tmp in {0, 1}:
        #         result = f'{tmp}{result}'
        #         carry = 0
        #     else:
        #         num = tmp % 2
        #         result = f'{num}{result}'
        #         carry = 1
        #     a = a[:-1] if a else ''
        #     b = b[:-1] if b else ''
        #
        # if carry:
        #     result = f'{carry}{result}'
        # return result

        a = int(a, 2)
        b = int(b, 2)
        return '{0:b}'.format(a + b)
