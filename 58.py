class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = 0
        ans = 0
        for char in s:
            if char == ' ':
                ans = tmp if tmp != 0 else ans
                tmp = 0
            else:
                tmp += 1
        ans = tmp if tmp != 0 else ans
        return ans
