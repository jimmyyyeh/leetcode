class Solution:
    """
    兩種解題思路:
    1. 起始點為h, 往右查找>=h的即為終點端, 累加區域; 當查找到max高度時, 則反轉剩下區域繼續, 確保整體高度是升冪走勢
    2. 每一個元素依序尋找左邊及右邊的最高值(包含自己, 若有一側小於自己, 則無法形成面積, 視為0), 當前的值-min(左邊, 右邊)=此高度會形成的面積
    """

    # @staticmethod
    # def get_area(max_, height, ans):
    #     index = 0
    #     while index < len(height):
    #         h = height[index]
    #         if max_ == h:
    #             break
    #         stack = height[index + 1:]
    #         index_ = 0
    #         while stack:
    #             next_ = stack.pop(0)
    #             ans += h - next_ if h - next_ >= 0 else 0
    #             if next_ >= h:
    #                 next_index = index + index_ + 1
    #                 index = next_index
    #                 break
    #             index_ += 1
    #         if not stack:
    #             index += 1
    #     return ans, index
    #
    # def trap(self, height: List[int]) -> int:
    #     ans = 0
    #     if len(height) == 1:
    #         return 0
    #     max_ = max(height)
    #     ans, index = self.get_area(max_=max_, height=height, ans=ans)
    #     height = height[index:]
    #     height.reverse()
    #     max_ += 1  # 避免凹字型題型被直接break掉, 如[2, 0, 2]
    #     ans, index = self.get_area(max_=max_, height=height, ans=ans)
    #     return ans

    def trap(self, height: List[int]) -> int:
        if not list:
            return 0
        left_max = right_max = - 1
        left_list = list()
        right_list = list()
        for h in height:
            left_max = max(h, left_max)
            left_list.append(left_max)

        for h in reversed(height):
            right_max = max(h, right_max)
            # right_list.insert(0, right_max)
            # 如果用insert則不用逆序, 但insert效能較差
            right_list.append(right_max)

        right_list.reverse()
        ans = 0
        for index, h in enumerate(height):
            left = left_list[index]
            right = right_list[index]
            ans += min(left, right) - h
        return ans
