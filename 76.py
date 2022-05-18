class Solution:
    """
    以範例來看: ADOBECODEBANC,
    先從左邊找到第一個index, 為left指標, 接著找到第一組解: ADOBEC,
    此時再移動右邊指針 ADOBEC ODEB, 當碰到重複元素時, 移動左邊指針找到新的left, CODEBA,
    再繼續移動右邊指針
    """
    def minWindow(self, s: str, t: str) -> str:
        counter = dict()
        for char in t:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        ans = ''
        satisfy_num = 0
        left = 0

        for right, char in enumerate(s):
            if char not in counter:
                continue
            counter[char] -= 1
            if counter[char] == 0:
                satisfy_num += 1

            while s[left] not in counter or counter[s[left]] < 0:
                if s[left] in counter:
                    counter[s[left]] += 1
                left += 1
            if satisfy_num == len(counter):
                sub_str = s[left: right + 1]
                ans = sub_str if not ans or len(sub_str) < len(ans) else ans
        return ans
