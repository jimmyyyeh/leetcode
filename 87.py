from collections import Counter


class Solution:
    """
    TODO
    概念是二元樹反轉, 剪枝, 以範例而言, 參考下解:
    https://www.youtube.com/watch?v=sETxfdHwxc0

    abcde
    如果不反轉, 就是比較:
    s1 [0, 1, 2, 3...l-1] [k, k+1, k+2, .... l-1]
    s2 [0, 1, 2, 3...l-1] [k, k+1, k+2, .... l-1]
    如果反轉, 必須限制"兩個字段的長度要相同", 因此切割後要再做交換:

    s1 [0, 1, 2, 3...l-1] [k, k+1, k+2, .... l-1]
    s2 [0, 1, 2, 3...l-k-1] [l-k, l-k+1, l-k+2, .... l-1]
    -> 交換比較
    s1 [0, 1, 2, 3...l-1] [k, k+1, k+2, .... l-1]
    s2 [l-k, l-k+1, l-k+2, .... l-1] [0, 1, 2, 3...l-k-1]
    """
    def helper(self, s1, s2, dp):
        if (s1, s2) in dp:
            return dp[(s1, s2)]
        if s1 == s2:
            dp[(s1, s2)] = True
            return True
        if Counter(s1) != Counter(s2):
            dp[(s1, s2)] = False
            return False

        len_ = len(s1)
        for i in range(1, len_):
            if self.helper(s1=s1[:i], s2=s2[:i], dp=dp) and self.helper(s1=s1[i:], s2=s2[i:], dp=dp):
                dp[(s1, s2)] = True
                return True
            if self.helper(s1=s1[:i], s2=s2[len_ - i:], dp=dp) and self.helper(s1=s1[i:], s2=s2[:len_ - i], dp=dp):
                dp[(s1, s2)] = True
                return True
        dp[(s1, s2)] = False
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        return self.helper(s1=s1, s2=s2, dp=dict())
