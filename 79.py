class Solution:
    #
    # @staticmethod
    # def get_direction(x, y, m, n, path):
    #     direction = list()
    #     direction.append([x, y - 1]) if y > 0 and [x, y - 1] not in path else None  # 左
    #     direction.append([x, y + 1]) if y < n - 1 and [x, y + 1] not in path else None  # 右
    #     direction.append([x - 1, y]) if x > 0 and [x - 1, y] not in path else None  # 上
    #     direction.append([x + 1, y]) if x < m - 1 and [x + 1, y] not in path else None  # 下
    #     return direction
    #
    # def dfs(self, board, x, y, word, m, n, path, word_len):
    #     if len(path) == word_len:
    #         return
    #     current = board[x][y]
    #     if current == word[0]:
    #         path.append([x, y])
    #         if len(path) == word_len:
    #             return
    #         direction = self.get_direction(x=x, y=y, m=m, n=n, path=path)
    #         for d in direction:
    #             x_, y_ = d
    #             self.dfs(board=board, x=x_, y=y_, word=word[1:], m=m, n=n, path=path, word_len=word_len)
    #             if len(path) == word_len:
    #                 return
    #         if path:
    #             path.pop()
    #
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     m, n = len(board), len(board[0])
    #     x = y = 0
    #     path = list()
    #     word_len = len(word)
    #     while x < m and y < n:
    #         self.dfs(board=board, x=x, y=y, word=word, m=m, n=n, path=path, word_len=word_len)
    #         if y == n - 1:
    #             y = -1
    #             x += 1
    #         y += 1
    #     return len(path) == word_len
    @staticmethod
    def is_bound(x, y, m, n):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1

    def dfs(self, board, m, n, x, y, index, word):
        if index == len(word):
            return True
        if not self.is_bound(x=x, y=y, m=m, n=n) or board[x][y] != word[index]:
            # 超出邊界 or 該位置不符合word需求
            return False

        board[x][y] = '-'
        is_finished = \
            self.dfs(board=board, m=m, n=n, x=x - 1, y=y, index=index + 1, word=word) or \
            self.dfs(board=board, m=m, n=n, x=x + 1, y=y, index=index + 1, word=word) or \
            self.dfs(board=board, m=m, n=n, x=x, y=y - 1, index=index + 1, word=word) or \
            self.dfs(board=board, m=m, n=n, x=x, y=y + 1, index=index + 1, word=word)
        board[x][y] = word[index]

        return is_finished

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    if self.dfs(board=board, m=m, n=n, x=x, y=y, index=0, word=word):
                        return True
        return False
