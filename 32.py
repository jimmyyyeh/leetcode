class Solution:
    """
    兩種解題思路:
    1. 由左至右用stack的方式做驗證, 找出最長的pattern, 接著截去第一個字符
    2. 由左至右, 由右至左, 各做一次, 當遇到"("則為+1, ")"則為-1, 當遇到pair_count<0即表示不能再湊成對, 則計數歸零
    """

    # @staticmethod
    # def valid(s, ans):
    #     """
    #     找出由左至右最長的pattern
    #     """
    #     stack = list()
    #     index_stack = list()
    #     for index, char_ in enumerate(s):
    #         if char_ == '(':
    #             stack.append('(')
    #             index_stack.append(index)
    #         else:
    #             if not stack:
    #                 return max(ans, (len(s[:index])))
    #             stack.pop()
    #             index_stack.pop()
    #     if stack:
    #         return max(ans, len(s[:index_stack[0]]))
    #     else:
    #         return max(ans, len(s))
    #
    # def longestValidParentheses(self, s: str) -> int:
    #     if not ('(' in s and ')' in s) or not s:
    #         return 0
    #     close_index = s.index(')')
    #     left = s[close_index:]
    #     if '(' in left:
    #         next_start_index = left.index('(')
    #         redundant = close_index - next_start_index - 1
    #         redundant = 0 if redundant < 0 else redundant
    #         s = s[redundant:]
    #     # 去除左邊多餘的
    #
    #     ans = 0
    #     while s:
    #         if ans >= len(s):
    #             break
    #         ans = self.valid(s=s, ans=ans)
    #         s = s[1:]
    #     return ans
    @staticmethod
    def get_max_len(s, symbol):
        max_len = 0  # 緩存目前最大長度
        pair_count = 0  # 計算成對用, 當pair_count=0, 則表示成對配對
        current_count = 0  # 計算當前配對共有幾個符號
        for char_ in s:
            if char_ == symbol:
                pair_count += 1
            else:
                pair_count -= 1
            current_count += 1
            if pair_count == 0:
                max_len = max(max_len, current_count)
            elif pair_count < 0:
                current_count = 0
                pair_count = 0
        return max_len

    def longestValidParentheses(self, s: str) -> int:
        return max(self.get_max_len(s=s, symbol='('), self.get_max_len(s=s[::-1], symbol=')'))
