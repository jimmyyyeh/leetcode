class Solution:
    """
    TODO
    動態規劃, 需要多理解, 參考下解:
    https://leetcode.com/problems/regular-expression-matching/discuss/314237/
    https://leetcode.com/problems/regular-expression-matching/discuss/336345/
    當前pattern = '.' or 當前字元 -> True case1
    當前pattern = '*'
        - 前一元素 = 當前元素 -> *重複使用 (當作 1 or 多個 p-1 使用) case2
        - 前一元素 != 當前元素 -> 忽略前一pattern (當作 0 個 p-1 使用) case3
    """
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        # 邊界問題1: (0, 0) 表示s, p同時為空
        dp[0][0] = True

        # 邊界問題2: s為空, ( , a*b*c) 也是可以匹配的
        for p_index in range(1, len_p + 1):
            if p[p_index - 1] == '*':
                dp[0][p_index] = dp[0][p_index - 2]

        for s_index in range(1, len_s + 1):
            for p_index in range(1, len_p + 1):
                if p[p_index - 1] == '*':
                    if p[p_index - 2] in {'.', s[s_index - 1]}:
                        # 前一pattern = . or 當前元素, 代表有出現>=1次 case2
                        # dp[s_index][p_index - 2]已經配對過1個(>1) or dp[s_index - 1][p_index]配對到第一個(=1)
                        dp[s_index][p_index] = dp[s_index][p_index - 2] or dp[s_index - 1][p_index]
                    else:
                        # 前一pattern沒有出現, 忽略前一pattern不計 case3
                        dp[s_index][p_index] = dp[s_index][p_index - 2]
                    # dp[s_index][p_index] = dp[s_index][p_index - 2]
                    # if p[p_index - 2] in {'.', s[s_index - 1]}:
                    #     dp[s_index][p_index] = dp[s_index][p_index] or dp[s_index - 1][p_index]
                else:
                    if p[p_index - 1] in {'.', s[s_index - 1]}:
                        # pattern = . or 當前元素 case1
                        dp[s_index][p_index] = dp[s_index - 1][p_index - 1]
                    # else:
                    #     dp[s_index][p_index] = False
        return dp[len_s][len_p]
