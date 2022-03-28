import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(p)
        return pattern.fullmatch(s)
