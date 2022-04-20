class Solution:
    @staticmethod
    def get_next(str_):
        ans = ''
        count = 1
        char_ = ''
        for index, char_ in enumerate(str_[:-1]):
            next_ = str_[index + 1]
            if char_ == next_:
                count += 1
            else:
                ans += f'{count}{char_}'
                count = 1

        if count == 1:
            ans += f'{count}{str_[-1]}'
        else:
            ans += f'{count}{char_}'
        return ans

    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(1, n):
            ans = self.get_next(str_=ans)
        return ans
