class Solution:
    """
    TODO
    動態規劃, 參考下解:
    https://www.youtube.com/watch?v=XYi2-LPrwm4
    大概概念如下:
    i, j表示word1[i]與word2[j]的字元比較, 即i, j = word1, word2的pointer
    - 如果兩者相等: dp[i][j] = dp[i+1][j+1], 兩個pointer都向前推進
    - 如果兩者不等: 則三選一(insert, replace, remove)操作, 選擇最小的方式做前進
        insert: 將word2[j]字元insert到word1, j+1, i不變
        replace: 將word2[j]字元replace到word1, j+1, i+1
        remove: 將word1[i]字元刪除, j不變, i+1

    dp矩陣從右下角開始依序往左上做, 要逆過來做也可以
    """
    def minDistance(self, word1: str, word2: str) -> int:
        len_1 = len(word1)
        len_2 = len(word2)
        if not (len_1 and len_2):
            return len_1 or len_2
        dp = [[2 ** 31 - 1] * (len_2 + 1) for _ in range(len_1 + 1)]

        # 處理邊境條件, 如果word1 or word2為空字串互相比較時
        for i in range(len_1 + 1):
            dp[i][len_2] = len_1 - i

        for j in range(len_2 + 1):
            dp[len_1][j] = len_2 - j

        for i in range(len_1 - 1, -1, -1):
            for j in range(len_2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = dp[i][j + 1]
                    replace = dp[i + 1][j + 1]
                    remove = dp[i + 1][j]
                    dp[i][j] = 1 + min([insert, replace, remove])
                    # 1表示當前的操作, 所以要加上1
        return dp[0][0]
