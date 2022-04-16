class Solution:
    """
    輸入 s = 'barfoothefoobarman', words = ['foo','bar']
    先依序將字串取出對應長度, 再將slice的字串轉成排序後的陣列, 與題目排序後比對相同則符合
    barfoo | thefoobarman -> ['bar', 'foo']
    arfoot | hefoobarman -> ['arf', 'oot']
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words = sorted(words)
        words_len = len(words)
        sub_len = len(words[0])
        step = sub_len * words_len

        index = 0
        ans = list()
        while len(s) >= step:
            sub_str = s[:step]
            s = s[1:]
            sub_str_list = [sub_str[sub_len * i: sub_len * i + sub_len] for i in range(words_len)]
            sub_str_list = sorted(sub_str_list)
            if sub_str_list == words:
                ans.append(index)
            index += 1
        return ans
