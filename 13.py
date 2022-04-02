class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        skip = False
        for index, char_ in enumerate(s):
            if skip:
                skip = False
                continue
            if index == len(s) - 1:
                next_roman_num = 0
            else:
                next_char = s[index + 1]
                next_roman_num = roman_dict[next_char]

            roman_num = roman_dict[char_]
            if roman_num >= next_roman_num:
                ans += roman_num
            else:
                ans += next_roman_num - roman_num
                skip = True
        return ans
