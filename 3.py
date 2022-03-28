class Solution(object):
    """
    TODO
    1. 每個字元一定要走完
    2. 遇到重複的字元就往前刪除 直到不重複為止
    """
    def lengthOfLongestSubstring(self, s):
        if len(set(s)) == len(s):
            return len(set(s))
        
        sub_str = ''
        ans = 0
        
        for char_ in s:
            while char_ in sub_str:
                sub_str = sub_str[1:]
            else:
                sub_str += char_
                ans = max(len(sub_str), ans)
        
        return ans
