class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True
        #         elif matrix[i][j] > target:
        #             return False

        # for index, row in enumerate(matrix):
        #     if row[0] > target:
        #         return target in matrix[index - 1]
        # return target in matrix[-1]

        # for index, row in enumerate(matrix):
        #     if row[0] > target:
        #         for column in matrix[index - 1]:
        #             if column == target:
        #                 return True
        #         return False
        #
        # for column in matrix[-1]:
        #     if column == target:
        #         return True
        # return False

        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and 0 <= j:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
