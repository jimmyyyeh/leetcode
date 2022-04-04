class Solution:
    """
    TODO
    1. 面積 = 矮的 * 兩者間隔數 (area = x * y)
    2. 較矮的向內移動, 保持高的(使x增加), 面積才有可能越來越大
    """
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        ans = 0
        while start < end:
            area = (end - start) * min(height[start], height[end])
            ans = area if area > ans else ans
            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1
                end -= 1
        return ans
