class Solution:
    @staticmethod
    def get_slope(element, n, slope_dict):
        if not element:
            return list()
        slope_set = set()
        x, y = element
        while x < n - 1 and y > 0:
            x += 1
            y -= 1
            slope_set.add((x, y))

        x, y = element
        while x < n - 1 and y < n - 1:
            x += 1
            y += 1
            slope_set.add((x, y))

        slope_dict[tuple(element)] = slope_set
        return slope_set

    def dfs(self, matrix, index, n, slope_dict, result, results):
        if index == n:
            # 走到最後一排
            results.append(result.copy())
            result.pop()
            return

        previous_column = set()  # 先前已經選過的column
        slope = set()  # 先前所有選擇棋格的斜率連集
        for r in result:
            row, column = r
            slope = slope | slope_dict.get((row, column), set()) if result else set()
            previous_column.add(column)

        next_ = matrix[index * n: (index + 1) * n]
        next_ = [n for n in next_ if n not in slope and n[1] not in previous_column]
        # 針對條件過濾

        for current in next_:
            row, column = current
            result.append(current)
            previous_column.add(column)
            self.dfs(matrix=matrix,
                     index=index + 1,
                     n=n,
                     slope_dict=slope_dict,
                     result=result,
                     results=results)
        if result:
            result.pop()
        return

    def totalNQueens(self, n: int) -> int:
        matrix = [(i, j) for i in range(n) for j in range(n)]
        slope_dict = dict()  # 存放每個點上的斜線
        for element in matrix[:-n]:
            self.get_slope(element=element, n=n, slope_dict=slope_dict)

        index = 0
        result = list()
        results = list()
        self.dfs(matrix=matrix,
                 index=index,
                 n=n,
                 slope_dict=slope_dict,
                 result=result,
                 results=results)
        return len(results)
