class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        遞迴字串頭尾一定為相同的字元
        因此每遇到一個字元 若和先前字元重複 擷取兩字元間並判斷是否為遞迴字串
        例如 abcccbba
        a -> abcccbba
        b -> bcccb / bcccbb
        c -> cc / cc
        """
        ans = ''
        position_dict = dict()
        for index, char_ in enumerate(s):
            if char_ not in position_dict:
                position_dict[char_] = list()
                if not ans:
                    # 若input各字元皆為獨立 則可隨意挑一字串做解
                    ans = char_
            else:
                for p in position_dict[char_]:
                    if index - p < len(ans):
                        # 被切掉的字串長度小於解 就不可能成為新的解
                        continue
                    check_str = s[p: index + 1]
                    if check_str == check_str[::-1]:
                        ans = check_str if len(check_str) > len(ans) else ans
            position_dict[char_].append(index)
        return ans
