class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = list()
        while True:
            ans.extend(matrix.pop(0))
            if not matrix:
                break

            for m in matrix:
                ans.append(m.pop())
                if not m:
                    matrix = matrix[1:]
            if not matrix:
                break

            ans.extend(matrix.pop()[::-1])
            if not matrix:
                break

            for m in reversed(matrix):
                ans.append(m.pop(0))
                if not m:
                    matrix = matrix[:-1]
            if not matrix:
                break
        return ans
