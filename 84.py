class Solution:
    """
    TODO
    暴力解法概念:
    (往左找第一個<自己的個數 + 往右找第一個<自己的個數)為底, *本身為高
    -> 嚴格遞增的stack(Monotonic stack), 遇到破壞規則的元素pop出來做計算
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0

        stack = list()
        heights.append(-1)  # 最後要遍歷所有還存在的stack, 因此多加一個最小元素
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                # 表示走到當前元素已經沒辦法走時, 計算先前stack內的元素所有可能的最大面積
                h = heights[stack.pop()]
                w = index - stack[-1] - 1 if stack else index
                area = w * h
                ans = area if area > ans else ans
            stack.append(index)
        return ans
