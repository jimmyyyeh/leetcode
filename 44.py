class Solution:
    """
    TODO:
    兩種解題思路
    1. two pointer 基本上會遇到下列的情形:
        a. 一對一的情形, 如 [abc, a?c], 則直接往後推進, 基本上沒問題
        b. 但如果遇到*會出現下列情形:
            如[abcdeabcdeabczz, *abczz], 要刪去的是哪一組abc之前的字串?
            因此當遇到*, 先緩存當前位置, 若走到沒辦法繼續往前時, 則回到s的緩存指標,
            接著向後推進一個位置(迫使s必須往後推進比對), p則回到緩存指標(即*)
    2. DP 需要多理解, 參考下解:
        https://leetcode.com/problems/wildcard-matching/discuss/321724/
        邊界:
        a. dp[0][0] -> s = '', p = '' (兩者皆為空字串)
            -> True
        b. dp[s_index][0] -> s = '...', p = '' (p為空字串)
            -> False
        c. dp[0][p_index] -> s = '', p = '....' (s為空字串)
            -> 依序判斷p直到遇到第一個非*為止, 如 s = '' 匹配 p = '*******.abc', 前面的*都可忽略不計
    """
    def isMatch(self, s: str, p: str) -> bool:
        # s_index = p_index = 0
        # p_tmp_index = s_tmp_index = None
        # s_len, p_len = len(s), len(p)
        # while s_index < s_len:
        #     if p_index < p_len and p[p_index] in {s[s_index], '?'}:
        #         s_index += 1
        #         p_index += 1
        #     elif p_index < p_len and p[p_index] == '*':
        #         p_index += 1
        #         s_tmp_index, p_tmp_index = s_index, p_index
        #     elif p_tmp_index is not None:
        #         s_tmp_index += 1
        #         s_index, p_index = s_tmp_index, p_tmp_index
        #     else:
        #         return False
        # return len(p[p_index:].replace('*', '')) == 0
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]

        dp[0][0] = True

        for p_index in range(1, len_p + 1):
            p_current = p[p_index - 1]
            if p_current != '*':
                break
            dp[0][p_index] = True

        for s_index in range(1, len_s + 1):
            s_current = s[s_index - 1]
            for p_index in range(1, len_p + 1):
                p_current = p[p_index - 1]
                if p_current in {s_current, '?'}:
                    dp[s_index][p_index] = dp[s_index - 1][p_index - 1]
                elif p_current == '*':
                    # dp[s_index - 1][p_index] match 至少一個 -> s = 'ccde', p = 'c*de'
                    # -> s[:s_index][:p_index-1], 參照s[:1] 與 p[:0] -> c 與 c, * 視為 c
                    # dp[s_index][p_index - 1] match 0 -> s = 'bde', p = 'b*de' (忽略不計*)
                    # -> s[:s_index-1][:p_index], 參照s[:0] 與 p[:1] -> b 與 b, * 忽略不計
                    dp[s_index][p_index] = dp[s_index - 1][p_index] or dp[s_index][p_index - 1]
                # else:
                #     dp[s_index][p_index] = False
        return dp[len_s][len_p]
