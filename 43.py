class Solution:
    """
    模擬直式除法, 用ord()取代int()將字串轉為數字
    """

    # def multiply(self, num1: str, num2: str) -> str:
    #     return str(int(num1) * int(num2))
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        num1_ = num1[::-1]
        num2_ = num2[::-1]

        ans = 0
        for index, char1 in enumerate(num1_):
            carry = 0  # 進位數
            power = 0  # 位數
            tmp = 0  # 當前數字列
            for char2 in num2_:
                num_ = (ord(char1) - ord('0')) * (ord(char2) - ord('0')) + carry
                carry = num_ // 10
                tmp += num_ % 10 * 10 ** power
                power += 1
            if carry:
                tmp += carry * 10 ** power
            ans += tmp * 10 ** index
        return f'{ans}'
