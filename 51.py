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

    def solveNQueens(self, n: int) -> list[list[str]]:
        matrix = [(i, j) for i in range(n) for j in range(n)]
        result = list()
        results = list()
        slope_list = list()  # 存放已走過點的斜率
        slope_dict = dict()  # 存放每個點上的斜線
        blocked = list()
        previous_column = set()
        for element in matrix[:-n]:
            self.get_slope(element=element, n=n, slope_dict=slope_dict)

        while True:
            row = len(result)
            current = matrix[row * n: (row + 1) * n]
            current = [c for c in current if c not in slope_list + blocked and c[1] not in previous_column]
            if not current:
                if row == 0:
                    break
                element = (len(result) - 1, result[-1].index('Q'))
                result.pop()
                previous_column.remove(element[1])
                slope = slope_dict.get(tuple(element))
                slope_list = slope_list[:-len(slope)] if slope else slope_list
                blocked.append(element)
                continue
            element = current[0]
            result.append('.' * (element[1]) + 'Q' + '.' * (n - element[1] - 1))
            previous_column.add(element[1])
            if len(result) == n:
                results.append(result.copy())
            else:
                slope = slope_dict.get(tuple(element))
                slope_list.extend(slope)
                blocked = [u for u in blocked if u[0] <= element[0]]
        return results
