import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        pattern = re.compile(r'^[+-]?[\d]+')
        valid = pattern.search(s)
        if not valid:
            return 0
        ans = valid.group()
        ans = int(ans)
        max_ = 2 ** 31 - 1
        min_ = -2 ** 31
        if ans > max_:
            return max_
        elif ans < min_:
            return min_
        else:
            return ans
