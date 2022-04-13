class Solution:
    """
    兩種解題思路:
    1. 總共會走n * 2層的tree
       如果不符合條件就不繼續走下去
       -> 左括號的數量<右括號 or 其中一個括號的數量>n 為不符合
    2. 左邊括號先用完(l-1), 當兩個括號都用完時會退回第一次遞減l的地方去遞減r(r-1)
    """

    # @staticmethod
    # def validate(str_, n, symbol):
    #     if str_.count(symbol) > n:
    #         return False
    #     left_count = 0
    #     right_count = 0
    #     for char_ in str_:
    #         if char_ == '(':
    #             left_count += 1
    #         else:
    #             right_count += 1
    #         if left_count < right_count:
    #             return False
    #     return True
    #
    # def generateParenthesis(self, n: int) -> List[str]:
    #     results = ['']
    #     for i in range(n * 2):
    #         tmp_left = [f'{result}(' for result in results if self.validate(str_=f'{result}(', n=n, symbol='(')]
    #         tmp_right = [f'{result})' for result in results if self.validate(str_=f'{result})', n=n, symbol=')')]
    #         results = tmp_left + tmp_right
    #     return results

    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, left, right, item, res):
        if right < left:
            return
        if left == 0 and right == 0:
            res.append(item)
            # 退回第一個 l - 1的地方 繼續做 r -1
        if left > 0:
            self.helper(left - 1, right, item + '(', res)
        if right > 0:
            self.helper(left, right - 1, item + ')', res)
