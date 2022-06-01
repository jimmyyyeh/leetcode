class Solution:
    """
    TODO
    dp, 類似Wildcard Matching, 看見字串比對可以直接考慮用dp去做, 參考下解:
    https://www.youtube.com/watch?v=3Rw3p9LrgvE
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        if len_1 + len_2 != len_3:
            return False

        dp = [[False] * (len_2 + 1) for _ in range(len_1 + 1)]
        dp[len_1][len_2] = True

        for index_1 in range(len_1, -1, -1):
            for index_2 in range(len_2, -1, -1):
                if index_1 < len_1 and s1[index_1] == s3[index_1 + index_2] and dp[index_1 + 1][index_2]:
                    dp[index_1][index_2] = True
                if index_2 < len_2 and s2[index_2] == s3[index_1 + index_2] and dp[index_1][index_2 + 1]:
                    dp[index_1][index_2] = True
        return dp[0][0]
