class Solution:
    """
    兩種解題思路:
    1. 每個字串內一定會有一組是相鄰配對, 每遇到第一組配對成功的, 就移除該組, 直到無法移除為止
    2. stack
    """
    def isValid(self, s: str) -> bool:
        # left = ['(', '{', '[']
        # right = [')', '}', ']']
        # bracket_dict = dict(zip(left, right))
        #
        # s = list(s)
        # while s:
        #     is_couple = False
        #     for index, char_ in enumerate(s[:-1]):
        #         if char_ not in left:
        #             continue
        #         next_char = s[index + 1]
        #         if bracket_dict[char_] == next_char:
        #             del s[index]
        #             del s[index]
        #             is_couple = True
        #             break
        #     if not is_couple:
        #         return False
        # return True
        bracket_dict = dict(zip(['(', '{', '['], [')', '}', ']']))
        stack = []

        for char_ in s:
            if char_ in bracket_dict:
                stack.append(char_)
            elif len(stack) == 0:
                # 遇到了右字符, 且此時也沒有可以配對的左字符
                return False
            elif stack[-1] in bracket_dict and char_ != bracket_dict[stack[-1]]:
                # 遇到了右字符, 與stack最後遇到的左字符不對稱
                return False
            else:
                # 配對成功
                stack.pop()

        return len(stack) == 0
