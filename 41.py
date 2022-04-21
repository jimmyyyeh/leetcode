class Solution:
    """
    兩種解題思路:
    1. 先排序後依序找出n+1是否與n連續(時間複雜度因為sorted為nlogn, 不符合題目要求)
    2. 先列出所有可能的解, 接著迭代nums, 如果num有在可能解內, 則移除, 剩下最小的即為解
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = sorted(set(nums))
        # if 1 not in nums:
        #     # 如果1不在數列內, 最小的肯定為1
        #     return 1
        #
        # for index, num in enumerate(nums[:-1]):
        #     if num < 0:
        #         # 負數跳過不記
        #         continue
        #     if num + 1 != nums[index + 1]:
        #         # 判斷與下一個數是否相同
        #         return num + 1
        # # 若走到最後一個數, 即代表正數都為連續值, 則回傳max值+1
        # return nums[-1] + 1
        if 1 not in nums:
            return 1
        next_set = set(range(1, len(nums) + 2))
        for num in nums:
            if num in next_set:
                next_set.remove(num)
        return min(next_set)
