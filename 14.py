class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        min_str = strs[0]
        ans = ''
        for index, char_ in enumerate(min_str):
            count = 0
            for str_ in strs[1:]:
                if str_[index] != char_:
                    break
                else:
                    count += 1
            if count == len(strs) - 1:
                ans += char_
            else:
                break
        return ans
