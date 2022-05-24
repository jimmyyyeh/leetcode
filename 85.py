class Solution:
    """
    以序作每一個row, 就可以將每一個row看成是一個histogram,
    接著延續Largest Rectangle in Histogram, 去做解即可
    """

    @staticmethod
    def get_max_area(heights):
        """
        Largest Rectangle in Histogram
        """
        ans = 0

        stack = list()
        heights.append(-1)
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = index - stack[-1] - 1 if stack else index
                area = w * h
                ans = area if area > ans else ans
            stack.append(index)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        height_dict = dict()  # 儲存row中每一個元素的高度
        for i in range(m):
            heights = list()
            for j in range(n):
                if j not in height_dict:
                    height_dict[j] = 0
                if matrix[i][j] == '1':
                    height_dict[j] += 1
                else:
                    height_dict[j] = 0
                heights.append(height_dict[j])
            area = self.get_max_area(heights=heights)
            ans = area if area > ans else ans
        return ans
