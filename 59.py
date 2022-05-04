class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        x_step, y_step = 0, 1
        max_x = max_y = n - 1
        min_x, min_y = 0, 0
        current = [0, 0]
        matrix[0][0] = 1
        for i in range(2, n ** 2 + 1):
            current = [current[0] + x_step, current[1] + y_step]
            matrix[current[0]][current[1]] = i
            if y_step:
                if current[1] == max_y and current[0] == min_x:
                    min_x += 1  # x最小邊界增加
                    x_step, y_step = 1, 0
                elif current[1] == min_y and current[0] == max_x:
                    x_step, y_step = -1, 0
            else:
                if current[0] == max_x and current[1] == max_y:
                    x_step, y_step = 0, -1
                elif current[0] == min_x and current[1] == min_y:
                    min_y += 1  # y最小邊界增加
                    max_x -= 1  # x最大邊界減少
                    max_y -= 1  # y最大邊界減少
                    x_step, y_step = 0, 1
        return matrix
