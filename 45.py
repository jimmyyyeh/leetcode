class Solution:
    """
    TODO
    兩種解題思路:
    1. dp
        nums = [2, 3, 1, 1, 4] 為例
        先預設每個點走到終點的距離dp為[0, inf, inf, inf, inf](不一定要inf, 只要是不可能的極大數字即可)
        迭代nums:
            - 2 可以走到的範圍為 3, 1 -> 走一步, 此時dp = [0, 1, 1, inf, inf]
            - 3 可以走到的範圍為 1, 1, 4 -> 再走一步, 此時dp = [0, 1, 1, 2, 2] (因為index 1, 2走一步即可完成, 就不需要再走一步)
        依此類推, 走到終點為止
    2. greedy
        nums = [2, 3, 1, 1, 4] 為例
        edge_index = 當前邊界index(上次移動後最遠的距離)
        next_edge = 當前位置能跳到最遠的index
        當index == edge_index時, 表示必須得移動, 因此count += 1, 移動後的距離則是最遠距離next_edge
    """
    def jump(self, nums: List[int]) -> int:
        # len_ = len(nums)
        # dp = [len_ + 1] * len_
        # dp[0] = 0
        # for index, num in enumerate(nums):
        #     for index_ in range(1, num + 1):
        #         if index + index_ < len_:
        #             dp[index + index_] = min(dp[index + index_], dp[index] + 1)
        #
        # return dp[-1]

        len_ = len(nums)
        if len_ == 1:
            return 0

        distance = len_ - 1
        next_edge = edge_index = 0
        count = 0
        for index, num in enumerate(nums[:-1]):
            next_edge = max(next_edge, index + num)
            if index == edge_index:
                edge_index = next_edge
                count += 1
                if next_edge >= distance:
                    return count
        return count
